import os
import csv
from io import StringIO
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, make_response
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, get_car_data

app = Flask(__name__)

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Database
db = SQL("sqlite:///garage.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# --- GLOBAL CONTEXT: USER RANK ---


@app.context_processor
def inject_user_status():
    """Injects the user's rank/VIP status into every page template"""
    if session.get("user_id"):
        # Calculate total garage value for ranking
        result = db.execute(
            "SELECT SUM(price) as total FROM cars WHERE user_id = ?", session["user_id"])
        equity = result[0]["total"] or 0

        # Assign Rank
        if equity > 5000000:
            rank, color = "MAGNATE", "text-warning"
        elif equity > 1000000:
            rank, color = "VIP", "text-info"
        elif equity > 0:
            rank, color = "COLLECTOR", "text-success"
        else:
            rank, color = "ROOKIE", "text-secondary"

        return dict(user_rank=rank, rank_color=color)
    return dict(user_rank="", rank_color="")


# --- MAIN ROUTES ---

@app.route("/", methods=["GET"])
@login_required
def index():
    """Main Dashboard: Shows garage, search, and analytics"""
    user_id = session["user_id"]

    # Filter Logic
    search_q = request.args.get("q")
    cat_filter = request.args.get("category")

    query = "SELECT * FROM cars WHERE user_id = ?"
    params = [user_id]

    if search_q:
        query += " AND (make LIKE ? OR model LIKE ?)"
        params.extend([f"%{search_q}%", f"%{search_q}%"])

    if cat_filter and cat_filter != "All":
        query += " AND category LIKE ?"
        params.append(f"%{cat_filter}%")

    cars = db.execute(query, *params)

    # Attach service history and calculate stats
    all_services = db.execute(
        "SELECT * FROM services WHERE user_id = ? ORDER BY date DESC", user_id)

    for car in cars:
        # Get specific services for this car
        car["services"] = [s for s in all_services if s["car_id"] == car["id"]]

        # Calculate Total Invested (Price + Maintenance)
        maint_cost = sum(s["cost"] for s in car["services"])
        car["total_invested"] = (car["price"] or 0) + maint_cost

    # Dashboard Totals
    garage_equity = sum(c["total_invested"] for c in cars)
    formatted_equity = f"${garage_equity:,.0f}"

    # Get categories for the filter dropdown
    cats = db.execute(
        "SELECT DISTINCT category FROM cars WHERE user_id = ? ORDER BY category", user_id)
    category_list = [c["category"] for c in cats if c["category"]]

    return render_template("index.html",
                           cars=cars,
                           total_cars=len(cars),
                           total_value=formatted_equity,
                           categories=category_list)


@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    """Acquire a new car (supports AI Auto-fill)"""
    if request.method == "POST":
        make = request.form.get("make")
        model = request.form.get("model")

        # 1. Handle AI Auto-Fill Request
        if "auto_fill" in request.form:
            if not make or not model:
                return apology("Please enter Make and Model to auto-fill")

            # Fetch data from Gemini/Wikipedia
            ai_data = get_car_data(make, model)

            if ai_data:
                return render_template("add.html",
                                       pre_make=make,
                                       pre_model=model,
                                       data=ai_data,
                                       auto_image=ai_data.get("image_url", ""))
            else:
                return apology("AI could not find this car. Please enter manually.")

        # 2. Handle Final Save to Database
        if not make or not model:
            return apology("Make and Model are required")

        # Use Unsplash fallback if no image provided
        image_url = request.form.get("image")
        if not image_url:
            image_url = "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?auto=format&fit=crop&w=1000&q=80"

        db.execute("""
            INSERT INTO cars (user_id, make, model, year, rating, price, image, notes, category,
                            horsepower, top_speed, acceleration, engine)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, session["user_id"], make, model,
                   request.form.get("year"), request.form.get("rating"), request.form.get("price"),
                   image_url, request.form.get("notes"), request.form.get("category"),
                   request.form.get("horsepower"), request.form.get("top_speed"),
                   request.form.get("acceleration"), request.form.get("engine"))

        return redirect("/")

    return render_template("add.html")


@app.route("/add_service", methods=["POST"])
@login_required
def add_service():
    """Log a maintenance event"""
    if not request.form.get("description") or not request.form.get("cost"):
        return apology("Service details missing")

    db.execute("""
        INSERT INTO services (car_id, user_id, service_type, description, cost)
        VALUES (?, ?, ?, ?, ?)
    """, request.form.get("car_id"), session["user_id"],
               request.form.get("type"), request.form.get("description"), request.form.get("cost"))

    return redirect("/")


@app.route("/compare")
@login_required
def compare():
    """Battle Mode: Compare 2 or more cars"""
    selected_ids = request.args.getlist("id")

    if len(selected_ids) < 2:
        return redirect("/")

    # Dynamic SQL for multiple IDs
    placeholders = ', '.join(['?'] * len(selected_ids))
    query = f"SELECT * FROM cars WHERE id IN ({placeholders}) AND user_id = ?"
    params = selected_ids + [session["user_id"]]

    fighters = db.execute(query, *params)
    return render_template("compare.html", cars=fighters)


@app.route("/leaderboard")
@login_required
def leaderboard():
    """Global Rankings based on Garage Value"""
    users = db.execute("""
        SELECT users.username, COUNT(cars.id) as car_count, SUM(cars.price) as total_value
        FROM users
        JOIN cars ON users.id = cars.user_id
        GROUP BY users.id
        ORDER BY total_value DESC
        LIMIT 10
    """)

    for u in users:
        val = u["total_value"] or 0
        u["formatted_value"] = f"${val:,.0f}"

    return render_template("leaderboard.html", rankings=users)


@app.route("/profile")
@login_required
def profile():
    """Display User Profile Stats"""
    user_id = session["user_id"]

    # Get user details
    user = db.execute("SELECT username FROM users WHERE id = ?", user_id)[0]

    # Get stats
    cars = db.execute("SELECT price FROM cars WHERE user_id = ?", user_id)
    total_cars = len(cars)
    total_val = sum((c["price"] or 0) for c in cars)

    return render_template("profile.html",
                           username=user["username"],
                           total_cars=total_cars,
                           total_value=f"${total_val:,.0f}")


@app.route("/export")
@login_required
def export():
    """Export garage to CSV"""
    cars = db.execute(
        "SELECT make, model, year, price, horsepower, category FROM cars WHERE user_id = ?", session["user_id"])

    si = StringIO()
    cw = csv.writer(si)
    cw.writerow(["Make", "Model", "Year", "Value", "HP", "Category"])
    for car in cars:
        cw.writerow([car["make"], car["model"], car["year"],
                    car["price"], car["horsepower"], car["category"]])

    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=octane_vault.csv"
    output.headers["Content-type"] = "text/csv"
    return output


@app.route("/delete", methods=["POST"])
@login_required
def delete():
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM cars WHERE id = ? AND user_id = ?", id, session["user_id"])
    return redirect("/")


@app.route("/intro")
def intro():
    return render_template("intro.html")


# --- AUTH ROUTES ---

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        if not request.form.get("username") or not request.form.get("password"):
            return apology("Username and Password required", 403)

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("Invalid credentials", 403)

        session["user_id"] = rows[0]["id"]
        return redirect("/")

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = request.form.get("username")
        pw = request.form.get("password")
        confirm = request.form.get("confirmation")

        if not user or not pw or not confirm:
            return apology("All fields are required")
        if pw != confirm:
            return apology("Passwords do not match")

        try:
            hash = generate_password_hash(pw)
            new_user_id = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", user, hash)
            session["user_id"] = new_user_id
            return redirect("/")
        except ValueError:
            return apology("Username already taken")

    return render_template("register.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
