import os
import requests
import json
import re
from flask import redirect, render_template, session
from functools import wraps


def apology(message, code=400):
    def escape(s):
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def get_wiki_image(query):
    try:
        url = "https://en.wikipedia.org/w/api.php"
        headers = {'User-Agent': 'DreamGarage/1.0'}

        # Search for page
        params = {
            "action": "query", "list": "search", "srsearch": query,
            "format": "json", "srlimit": 1
        }
        search = requests.get(url, params=params, headers=headers, timeout=5).json()

        if not search.get("query", {}).get("search"):
            return None

        # Get image from page
        title = search["query"]["search"][0]["title"]
        img_params = {
            "action": "query", "titles": title, "prop": "pageimages",
            "pithumbsize": 1000, "format": "json"
        }
        data = requests.get(url, params=img_params, headers=headers, timeout=5).json()
        pages = data["query"]["pages"]

        for pid in pages:
            if "thumbnail" in pages[pid]:
                return pages[pid]["thumbnail"]["source"]
    except:
        return None


def get_fallback_data(make, model):
    data = {
        "year": 2023, "rating": 9, "price": 200000,
        "description": f"The {make} {model} is a high-performance vehicle known for engineering excellence.",
        "horsepower": 500, "top_speed": 180, "acceleration": 3.5,
        "engine": "V8 Turbo", "category": "Supercar"
    }

    overrides = {
        "f40": {"year": 1987, "price": 1000000, "horsepower": 471},
        "supra": {"year": 1998, "price": 80000, "category": "JDM Legend"},
        "p1": {"year": 2013, "price": 1150000, "category": "Hypercar"},
    }

    for k, v in overrides.items():
        if k in model.lower():
            data.update(v)
            break

    return data


def get_car_data(make, model):
    data = None
    api_key = os.environ.get("API_KEY")

    if api_key:
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
            prompt = f"Return JSON for '{make} {model}' with keys: price(int), year(int), category, description, horsepower(int), top_speed(int), acceleration(float), engine, rating(int). No markdown."

            payload = {"contents": [{"parts": [{"text": prompt}]}]}
            resp = requests.post(url, json=payload, headers={
                                 'Content-Type': 'application/json'}, timeout=6)

            if resp.status_code == 200:
                text = resp.json()['candidates'][0]['content']['parts'][0]['text']
                clean_text = re.sub(r"```json|```", "", text).strip()
                data = json.loads(clean_text)

                # Cleanup price format
                if isinstance(data.get("price"), str):
                    data["price"] = int(''.join(filter(str.isdigit, data["price"])))
        except:
            pass

    if not data:
        data = get_fallback_data(make, model)

    # Always try to fetch a real image
    data["image_url"] = get_wiki_image(
        f"{make} {model} car") or "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7"

    return data
