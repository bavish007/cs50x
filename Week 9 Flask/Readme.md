# Week 9 Flask

## 🎯 Overview

In this week, I transitioned from static HTML pages to building dynamic web applications using Python and Flask. The focus shifted to server-side programming, where I learned to handle user inputs, manage sessions, and interact with databases permanently.

**Top 3 Learning Outcomes:**

1. **Flask Framework**: Learned to use the Flask micro-framework to create web applications, route URLs to functions, and render HTML templates.
2. **MVC Architecture**: Explored the Model-View-Controller design pattern, managing data with SQL (Model), displaying content with HTML (View), and handling logic with Python (Controller).
3. **Data Persistence & Sessions**: Implemented functionality to store user data in SQL databases and maintain user state across different pages using cookies and sessions.

## 📚 Documentation & Resources

| Document | Type | Location |
| :--- | :---: | :--- |
| **Notes** | Markdown | [Lecture/Notes.md](./Lecture/Notes.md) |
| **AJAX Guide** | PDF | [Lecture/Additional Concepts/ajax.pdf](./Lecture/Additional%20Concepts/ajax.pdf) |
| **Flask Guide** | PDF | [Lecture/Additional Concepts/flask.pdf](./Lecture/Additional%20Concepts/flask.pdf) |
| **Lecture Slides** | PPTX | [Lecture/Resources/CS50 2025 - Lecture 9 - Flask.pptx](./Lecture/Resources/CS50%202025%20-%20Lecture%209%20-%20Flask.pptx) |
| **Lecture PDF** | PDF | [Lecture/Resources/lecture9.pdf](./Lecture/Resources/lecture9.pdf) |
| **Source Code PDF** | PDF | [Lecture/Source Code/src9.pdf](./Lecture/Source%20Code/src9.pdf) |
| **Section PDF** | PDF | [Section/Resources/section9.pdf](./Section/Resources/section9.pdf) |

## 🗂️ Complete File Index

<details><summary><b>📂 View Source Files</b></summary>

| File | Type | Link |
| :--- | :---: | :--- |
| 📂 **Lecture / Additional Concepts** | Folder | [View](./Lecture/Additional%20Concepts) |
| 📄 `ajax.pdf` | .pdf | [Download](./Lecture/Additional%20Concepts/ajax.pdf) |
| 📄 `flask.pdf` | .pdf | [Download](./Lecture/Additional%20Concepts/flask.pdf) |
| 📄 `Notes.md` | .md | [View](./Lecture/Notes.md) |
| 📂 **Lecture / Resources** | Folder | [View](./Lecture/Resources) |
| 📄 `CS50 2025 - Lecture 9 - Flask.pptx` | .pptx | [Download](./Lecture/Resources/CS50%202025%20-%20Lecture%209%20-%20Flask.pptx) |
| 📄 `lecture9.pdf` | .pdf | [Download](./Lecture/Resources/lecture9.pdf) |
| 📂 **Lecture / Source Code / src9 / froshims0** | Folder | [View](./Lecture/Source%20Code/src9/froshims0) |
| 📄 `app.py` | .py | [View](./Lecture/Source%20Code/src9/froshims0/app.py) |
| 📄 `requirements.txt` | .txt | [View](./Lecture/Source%20Code/src9/froshims0/requirements.txt) |
| 📄 `failure.html` | .html | [View](./Lecture/Source%20Code/src9/froshims0/templates/failure.html) |
| 📄 `index.html` | .html | [View](./Lecture/Source%20Code/src9/froshims0/templates/index.html) |
| 📄 `layout.html` | .html | [View](./Lecture/Source%20Code/src9/froshims0/templates/layout.html) |
| 📄 `success.html` | .html | [View](./Lecture/Source%20Code/src9/froshims0/templates/success.html) |
| 📂 **Lecture / Source Code / src9 / froshims1** | Folder | [View](./Lecture/Source%20Code/src9/froshims1) |
| 📄 `app.py` | .py | [View](./Lecture/Source%20Code/src9/froshims1/app.py) |
| 📄 `requirements.txt` | .txt | [View](./Lecture/Source%20Code/src9/froshims1/requirements.txt) |
| 📄 `failure.html` | .html | [View](./Lecture/Source%20Code/src9/froshims1/templates/failure.html) |
| 📄 `index.html` | .html | [View](./Lecture/Source%20Code/src9/froshims1/templates/index.html) |
| 📄 `layout.html` | .html | [View](./Lecture/Source%20Code/src9/froshims1/templates/layout.html) |
| 📄 `success.html` | .html | [View](./Lecture/Source%20Code/src9/froshims1/templates/success.html) |
| 📂 **Lecture / Source Code / src9 / froshims2** | Folder | [View](./Lecture/Source%20Code/src9/froshims2) |
| 📄 `app.py` | .py | [View](./Lecture/Source%20Code/src9/froshims2/app.py) |
| 📄 `requirements.txt` | .txt | [View](./Lecture/Source%20Code/src9/froshims2/requirements.txt) |
| 📄 `failure.html` | .html | [View](./Lecture/Source%20Code/src9/froshims2/templates/failure.html) |
| 📄 `index.html` | .html | [View](./Lecture/Source%20Code/src9/froshims2/templates/index.html) |
| 📄 `layout.html` | .html | [View](./Lecture/Source%20Code/src9/froshims2/templates/layout.html) |
| 📄 `success.html` | .html | [View](./Lecture/Source%20Code/src9/froshims2/templates/success.html) |
| 📂 **Lecture / Source Code / src9 / froshims3** | Folder | [View](./Lecture/Source%20Code/src9/froshims3) |
| 📄 `app.py` | .py | [View](./Lecture/Source%20Code/src9/froshims3/app.py) |
| 📄 `requirements.txt` | .txt | [View](./Lecture/Source%20Code/src9/froshims3/requirements.txt) |
| 📄 `cat.jpg` | .jpg | [View](./Lecture/Source%20Code/src9/froshims3/static/cat.jpg) |
| 📄 `error.html` | .html | [View](./Lecture/Source%20Code/src9/froshims3/templates/error.html) |
| 📄 `index.html` | .html | [View](./Lecture/Source%20Code/src9/froshims3/templates/index.html) |
| 📄 `layout.html` | .html | [View](./Lecture/Source%20Code/src9/froshims3/templates/layout.html) |
| 📄 `success.html` | .html | [View](./Lecture/Source%20Code/src9/froshims3/templates/success.html) |
| 📂 **Lecture / Source Code / src9 / froshims4** | Folder | [View](./Lecture/Source%20Code/src9/froshims4) |
| 📄 `app.py` | .py | [View](./Lecture/Source%20Code/src9/froshims4/app.py) |
| 📄 `requirements.txt` | .txt | [View](./Lecture/Source%20Code/src9/froshims4/requirements.txt) |
| 📄 `cat.jpg` | .jpg | [View](./Lecture/Source%20Code/src9/froshims4/static/cat.jpg) |
| 📄 `error.html` | .html | [View](./Lecture/Source%20Code/src9/froshims4/templates/error.html) |
| 📄 `index.html` | .html | [View](./Lecture/Source%20Code/src9/froshims4/templates/index.html) |
| 📄 `layout.html` | .html | [View](./Lecture/Source%20Code/src9/froshims4/templates/layout.html) |
| 📄 `registrants.html` | .html | [View](./Lecture/Source%20Code/src9/froshims4/templates/registrants.html) |
| 📂 **Lecture / Source Code / src9 / froshims5** | Folder | [View](./Lecture/Source%20Code/src9/froshims5) |
| 📄 `app.py` | .py | [View](./Lecture/Source%20Code/src9/froshims5/app.py) |
| 📄 `froshims.db` | .db | [View](./Lecture/Source%20Code/src9/froshims5/froshims.db) |
| 📄 `requirements.txt` | .txt | [View](./Lecture/Source%20Code/src9/froshims5/requirements.txt) |
| 📄 `cat.jpg` | .jpg | [View](./Lecture/Source%20Code/src9/froshims5/static/cat.jpg) |
| 📄 `error.html` | .html | [View](./Lecture/Source%20Code/src9/froshims5/templates/error.html) |
| 📄 `index.html` | .html | [View](./Lecture/Source%20Code/src9/froshims5/templates/index.html) |
| 📄 `layout.html` | .html | [View](./Lecture/Source%20Code/src9/froshims5/templates/layout.html) |
| 📄 `registrants.html` | .html | [View](./Lecture/Source%20Code/src9/froshims5/templates/registrants.html) |
| 📂 **Lecture / Source Code / src9 / froshims6** | Folder | [View](./Lecture/Source%20Code/src9/froshims6) |
| 📄 `app.py` | .py | [View](./Lecture/Source%20Code/src9/froshims6/app.py) |
| 📄 `froshims.db` | .db | [View](./Lecture/Source%20Code/src9/froshims6/froshims.db) |
| 📄 `requirements.txt` | .txt | [View](./Lecture/Source%20Code/src9/froshims6/requirements.txt) |
| 📄 `cat.jpg` | .jpg | [View](./Lecture/Source%20Code/src9/froshims6/static/cat.jpg) |
| 📄 `error.html` | .html | [View](./Lecture/Source%20Code/src9/froshims6/templates/error.html) |
| 📄 `index.html` | .html | [View](./Lecture/Source%20Code/src9/froshims6/templates/index.html) |
| 📄 `layout.html` | .html | [View](./Lecture/Source%20Code/src9/froshims6/templates/layout.html) |
| 📄 `registrants.html` | .html | [View](./Lecture/Source%20Code/src9/froshims6/templates/registrants.html) |
| 📂 **Lecture / Source Code / src9 / froshims7** | Folder | [View](./Lecture/Source%20Code/src9/froshims7) |
| 📄 `app.py` | .py | [View](./Lecture/Source%20Code/src9/froshims7/app.py) |
| 📄 `froshims.db` | .db | [View](./Lecture/Source%20Code/src9/froshims7/froshims.db) |
| 📄 `requirements.txt` | .txt | [View](./Lecture/Source%20Code/src9/froshims7/requirements.txt) |
| 📄 `cat.jpg` | .jpg | [View](./Lecture/Source%20Code/src9/froshims7/static/cat.jpg) |
| 📄 `error.html` | .html | [View](./Lecture/Source%20Code/src9/froshims7/templates/error.html) |
| 📄 `index.html` | .html | [View](./Lecture/Source%20Code/src9/froshims7/templates/index.html) |
| 📄 `layout.html` | .html | [View](./Lecture/Source%20Code/src9/froshims7/templates/layout.html) |
| 📄 `registrants.html` | .html | [View](./Lecture/Source%20Code/src9/froshims7/templates/registrants.html) |
| 📂 **Lecture / Source Code / src9 / hello0** | Folder | [View](./Lecture/Source%20Code/src9/hello0) |
| 📄 `app.py` | .py | [View](./Lecture/Source%20Code/src9/hello0/app.py) |
| 📄 `requirements.txt` | .txt | [View](./Lecture/Source%20Code/src9/hello0/requirements.txt) |
| 📂 **Lecture / Source Code / src9 / hello1** | Folder | [View](./Lecture/Source%20Code/src9/hello1) |
| 📄 `app.py` | .py | [View](./Lecture/Source%20Code/src9/hello1/app.py) |
| 📄 `requirements.txt` | .txt | [View](./Lecture/Source%20Code/src9/hello1/requirements.txt) |
| 📂 **Lecture / Source Code / src9 / hello2–hello10** | Folder | [View](./Lecture/Source%20Code/src9) |
| 📄 `app.py` *(hello2–hello10)* | .py | [Browse](./Lecture/Source%20Code/src9) |
| 📂 **Lecture / Source Code / src9 / login** | Folder | [View](./Lecture/Source%20Code/src9/login) |
| 📄 `app.py` | .py | [View](./Lecture/Source%20Code/src9/login/app.py) |
| 📄 `requirements.txt` | .txt | [View](./Lecture/Source%20Code/src9/login/requirements.txt) |
| 📄 `index.html` | .html | [View](./Lecture/Source%20Code/src9/login/templates/index.html) |
| 📄 `layout.html` | .html | [View](./Lecture/Source%20Code/src9/login/templates/layout.html) |
| 📄 `login.html` | .html | [View](./Lecture/Source%20Code/src9/login/templates/login.html) |
| 📂 **Lecture / Source Code / src9 / shows0–shows3** | Folder | [View](./Lecture/Source%20Code/src9) |
| 📄 `app.py`, `shows.db` *(shows0–shows3)* | .py/.db | [Browse](./Lecture/Source%20Code/src9) |
| 📂 **Lecture / Source Code / src9 / store** | Folder | [View](./Lecture/Source%20Code/src9/store) |
| 📄 `app.py` | .py | [View](./Lecture/Source%20Code/src9/store/app.py) |
| 📄 `requirements.txt` | .txt | [View](./Lecture/Source%20Code/src9/store/requirements.txt) |
| 📄 `store.db` | .db | [View](./Lecture/Source%20Code/src9/store/store.db) |
| 📄 `books.html` | .html | [View](./Lecture/Source%20Code/src9/store/templates/books.html) |
| 📄 `cart.html` | .html | [View](./Lecture/Source%20Code/src9/store/templates/cart.html) |
| 📄 `layout.html` | .html | [View](./Lecture/Source%20Code/src9/store/templates/layout.html) |
| 📄 `src9.pdf` | .pdf | [Download](./Lecture/Source%20Code/src9.pdf) |
| 📂 **Problem Set 9 / birthdays** | Folder | [View](./Problem%20Set%209/birthdays) |
| 📄 `app.py` | .py | [View](./Problem%20Set%209/birthdays/app.py) |
| 📄 `birthdays.db` | .db | [View](./Problem%20Set%209/birthdays/birthdays.db) |
| 📄 `styles.css` | .css | [View](./Problem%20Set%209/birthdays/static/styles.css) |
| 📄 `index.html` | .html | [View](./Problem%20Set%209/birthdays/templates/index.html) |
| 📂 **Problem Set 9 / finance** | Folder | [View](./Problem%20Set%209/finance) |
| 📄 `app.py` | .py | [View](./Problem%20Set%209/finance/app.py) |
| 📄 `finance.db` | .db | [View](./Problem%20Set%209/finance/finance.db) |
| 📄 `helpers.py` | .py | [View](./Problem%20Set%209/finance/helpers.py) |
| 📄 `requirements.txt` | .txt | [View](./Problem%20Set%209/finance/requirements.txt) |
| 📄 `styles.css` | .css | [View](./Problem%20Set%209/finance/static/styles.css) |
| 📄 `apology.html` | .html | [View](./Problem%20Set%209/finance/templates/apology.html) |
| 📄 `buy.html` | .html | [View](./Problem%20Set%209/finance/templates/buy.html) |
| 📄 `history.html` | .html | [View](./Problem%20Set%209/finance/templates/history.html) |
| 📄 `index.html` | .html | [View](./Problem%20Set%209/finance/templates/index.html) |
| 📄 `layout.html` | .html | [View](./Problem%20Set%209/finance/templates/layout.html) |
| 📄 `login.html` | .html | [View](./Problem%20Set%209/finance/templates/login.html) |
| 📄 `quote.html` | .html | [View](./Problem%20Set%209/finance/templates/quote.html) |
| 📄 `register.html` | .html | [View](./Problem%20Set%209/finance/templates/register.html) |
| 📄 `sell.html` | .html | [View](./Problem%20Set%209/finance/templates/sell.html) |
| 📂 **Section / Resources** | Folder | [View](./Section/Resources) |
| 📄 `section9.pdf` | .pdf | [Download](./Section/Resources/section9.pdf) |
| 📂 **Section / Source Code / birthdays** | Folder | [View](./Section/Source%20Code/birthdays) |
| 📄 `app.py` | .py | [View](./Section/Source%20Code/birthdays/app.py) |
| 📄 `birthdays.db` | .db | [View](./Section/Source%20Code/birthdays/birthdays.db) |
| 📄 `styles.css` | .css | [View](./Section/Source%20Code/birthdays/static/styles.css) |
| 📄 `index.html` | .html | [View](./Section/Source%20Code/birthdays/templates/index.html) |

</details>

## 🎥 Video Resources

### Main Lecture

<div align="center">

[![Lecture 9](https://img.youtube.com/vi/am7POvSZ4GE/0.jpg)](https://youtu.be/am7POvSZ4GE)

</div>

### 🧠 Concept Clips

* [Flask](https://youtu.be/X0dwkDh8kwA)
* [Ajax](https://youtu.be/dQcBs4S-wEQ)

## 🛠️ Problem Sets & Labs

### 🎂 Birthdays

A basic Flask application created to keep track of friends' birthdays. This problem set serves as an introduction to linking a database (SQLite) with a web application (Flask), handling `POST` requests, and rendering data dynamically.

### 💰 Finance

C$50 Finance is a comprehensive stock trading simulation project. It requires implementing a robust web application that allows users to:

* Register and log in.
* Get real-time stock quotes.
* Buy and sell stocks using virtual cash.
* View transaction history.
This project connects all major concepts: Flask routes, SQL database management, session authentication, and API integration.

---

<div align="center">
  <br />
  <a href="../README.md">
    <img src="https://img.shields.io/badge/Return_to_Master_Index-181717?style=for-the-badge&logo=github&logoColor=white" alt="Back to Master Index" />
  </a>
</div>
