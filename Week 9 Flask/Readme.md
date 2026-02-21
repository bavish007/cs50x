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

* 📂 **Week 9 Flask**
  * 📂 **Lecture**
    * 📂 **Additional Concepts**
      * 📄 [`ajax.pdf`](./Lecture/Additional%20Concepts/ajax.pdf)
      * 📄 [`flask.pdf`](./Lecture/Additional%20Concepts/flask.pdf)
    * 📄 [`Notes.md`](./Lecture/Notes.md)
    * 📂 **Resources**
      * 📄 [`CS50 2025 - Lecture 9 - Flask.pptx`](./Lecture/Resources/CS50%202025%20-%20Lecture%209%20-%20Flask.pptx)
      * 📄 [`lecture9.pdf`](./Lecture/Resources/lecture9.pdf)
    * 📂 **Source Code**
      * 📂 **src9**
        * 📂 **froshims0**
          * 📄 [`app.py`](./Lecture/Source%20Code/src9/froshims0/app.py)
          * 📄 [`requirements.txt`](./Lecture/Source%20Code/src9/froshims0/requirements.txt)
          * 📂 **templates**
            * 📄 [`failure.html`](./Lecture/Source%20Code/src9/froshims0/templates/failure.html)
            * 📄 [`index.html`](./Lecture/Source%20Code/src9/froshims0/templates/index.html)
            * 📄 [`layout.html`](./Lecture/Source%20Code/src9/froshims0/templates/layout.html)
            * 📄 [`success.html`](./Lecture/Source%20Code/src9/froshims0/templates/success.html)
        * 📂 **froshims1**
          * 📄 [`app.py`](./Lecture/Source%20Code/src9/froshims1/app.py)
          * 📄 [`requirements.txt`](./Lecture/Source%20Code/src9/froshims1/requirements.txt)
          * 📂 **templates**
            * 📄 [`failure.html`](./Lecture/Source%20Code/src9/froshims1/templates/failure.html)
            * 📄 [`index.html`](./Lecture/Source%20Code/src9/froshims1/templates/index.html)
            * 📄 [`layout.html`](./Lecture/Source%20Code/src9/froshims1/templates/layout.html)
            * 📄 [`success.html`](./Lecture/Source%20Code/src9/froshims1/templates/success.html)
        * 📂 **froshims2**
          * 📄 [`app.py`](./Lecture/Source%20Code/src9/froshims2/app.py)
          * 📄 [`requirements.txt`](./Lecture/Source%20Code/src9/froshims2/requirements.txt)
          * 📂 **templates**
            * 📄 [`failure.html`](./Lecture/Source%20Code/src9/froshims2/templates/failure.html)
            * 📄 [`index.html`](./Lecture/Source%20Code/src9/froshims2/templates/index.html)
            * 📄 [`layout.html`](./Lecture/Source%20Code/src9/froshims2/templates/layout.html)
            * 📄 [`success.html`](./Lecture/Source%20Code/src9/froshims2/templates/success.html)
        * 📂 **froshims3**
          * 📄 [`app.py`](./Lecture/Source%20Code/src9/froshims3/app.py)
          * 📄 [`requirements.txt`](./Lecture/Source%20Code/src9/froshims3/requirements.txt)
          * 📂 **static**
            * 📄 [`cat.jpg`](./Lecture/Source%20Code/src9/froshims3/static/cat.jpg)
          * 📂 **templates**
            * 📄 [`error.html`](./Lecture/Source%20Code/src9/froshims3/templates/error.html)
            * 📄 [`index.html`](./Lecture/Source%20Code/src9/froshims3/templates/index.html)
            * 📄 [`layout.html`](./Lecture/Source%20Code/src9/froshims3/templates/layout.html)
            * 📄 [`success.html`](./Lecture/Source%20Code/src9/froshims3/templates/success.html)
        * 📂 **froshims4**
          * 📄 [`app.py`](./Lecture/Source%20Code/src9/froshims4/app.py)
          * 📄 [`requirements.txt`](./Lecture/Source%20Code/src9/froshims4/requirements.txt)
          * 📂 **static**
            * 📄 [`cat.jpg`](./Lecture/Source%20Code/src9/froshims4/static/cat.jpg)
          * 📂 **templates**
            * 📄 [`error.html`](./Lecture/Source%20Code/src9/froshims4/templates/error.html)
            * 📄 [`index.html`](./Lecture/Source%20Code/src9/froshims4/templates/index.html)
            * 📄 [`layout.html`](./Lecture/Source%20Code/src9/froshims4/templates/layout.html)
            * 📄 [`registrants.html`](./Lecture/Source%20Code/src9/froshims4/templates/registrants.html)
        * 📂 **froshims5**
          * 📄 [`app.py`](./Lecture/Source%20Code/src9/froshims5/app.py)
          * 📄 [`froshims.db`](./Lecture/Source%20Code/src9/froshims5/froshims.db)
          * 📄 [`requirements.txt`](./Lecture/Source%20Code/src9/froshims5/requirements.txt)
          * 📂 **static**
            * 📄 [`cat.jpg`](./Lecture/Source%20Code/src9/froshims5/static/cat.jpg)
          * 📂 **templates**
            * 📄 [`error.html`](./Lecture/Source%20Code/src9/froshims5/templates/error.html)
            * 📄 [`index.html`](./Lecture/Source%20Code/src9/froshims5/templates/index.html)
            * 📄 [`layout.html`](./Lecture/Source%20Code/src9/froshims5/templates/layout.html)
            * 📄 [`registrants.html`](./Lecture/Source%20Code/src9/froshims5/templates/registrants.html)
        * 📂 **froshims6**
          * 📄 [`app.py`](./Lecture/Source%20Code/src9/froshims6/app.py)
          * 📄 [`froshims.db`](./Lecture/Source%20Code/src9/froshims6/froshims.db)
          * 📄 [`requirements.txt`](./Lecture/Source%20Code/src9/froshims6/requirements.txt)
          * 📂 **static**
            * 📄 [`cat.jpg`](./Lecture/Source%20Code/src9/froshims6/static/cat.jpg)
          * 📂 **templates**
            * 📄 [`error.html`](./Lecture/Source%20Code/src9/froshims6/templates/error.html)
            * 📄 [`index.html`](./Lecture/Source%20Code/src9/froshims6/templates/index.html)
            * 📄 [`layout.html`](./Lecture/Source%20Code/src9/froshims6/templates/layout.html)
            * 📄 [`registrants.html`](./Lecture/Source%20Code/src9/froshims6/templates/registrants.html)
        * 📂 **froshims7**
          * 📄 [`app.py`](./Lecture/Source%20Code/src9/froshims7/app.py)
          * 📄 [`froshims.db`](./Lecture/Source%20Code/src9/froshims7/froshims.db)
          * 📄 [`requirements.txt`](./Lecture/Source%20Code/src9/froshims7/requirements.txt)
          * 📂 **static**
            * 📄 [`cat.jpg`](./Lecture/Source%20Code/src9/froshims7/static/cat.jpg)
          * 📂 **templates**
            * 📄 [`error.html`](./Lecture/Source%20Code/src9/froshims7/templates/error.html)
            * 📄 [`index.html`](./Lecture/Source%20Code/src9/froshims7/templates/index.html)
            * 📄 [`layout.html`](./Lecture/Source%20Code/src9/froshims7/templates/layout.html)
            * 📄 [`registrants.html`](./Lecture/Source%20Code/src9/froshims7/templates/registrants.html)
        * 📂 **hello0**
          * 📄 [`app.py`](./Lecture/Source%20Code/src9/hello0/app.py)
          * 📄 [`requirements.txt`](./Lecture/Source%20Code/src9/hello0/requirements.txt)
        * 📂 **hello1**
          * 📄 [`app.py`](./Lecture/Source%20Code/src9/hello1/app.py)
          * 📄 [`requirements.txt`](./Lecture/Source%20Code/src9/hello1/requirements.txt)
        * 📂 **hello10**
          * 📄 [`app.py`](./Lecture/Source%20Code/src9/hello10/app.py)
          * 📄 [`requirements.txt`](./Lecture/Source%20Code/src9/hello10/requirements.txt)
          * 📂 **templates**
            * 📄 [`greet.html`](./Lecture/Source%20Code/src9/hello10/templates/greet.html)
            * 📄 [`index.html`](./Lecture/Source%20Code/src9/hello10/templates/index.html)
            * 📄 [`layout.html`](./Lecture/Source%20Code/src9/hello10/templates/layout.html)
        * 📂 **hello2**
          * 📄 [`app.py`](./Lecture/Source%20Code/src9/hello2/app.py)
          * 📄 [`requirements.txt`](./Lecture/Source%20Code/src9/hello2/requirements.txt)
          * 📂 **templates**
            * 📄 [`index.html`](./Lecture/Source%20Code/src9/hello2/templates/index.html)
        * 📂 **hello3**
          * 📄 [`app.py`](./Lecture/Source%20Code/src9/hello3/app.py)
          * 📄 [`requirements.txt`](./Lecture/Source%20Code/src9/hello3/requirements.txt)
          * 📂 **templates**
            * 📄 [`index.html`](./Lecture/Source%20Code/src9/hello3/templates/index.html)
        * 📂 **hello4**
          * 📄 [`app.py`](./Lecture/Source%20Code/src9/hello4/app.py)
          * 📄 [`requirements.txt`](./Lecture/Source%20Code/src9/hello4/requirements.txt)
          * 📂 **templates**
            * 📄 [`index.html`](./Lecture/Source%20Code/src9/hello4/templates/index.html)
        * 📂 **hello5**
          * 📄 [`app.py`](./Lecture/Source%20Code/src9/hello5/app.py)
          * 📄 [`requirements.txt`](./Lecture/Source%20Code/src9/hello5/requirements.txt)
          * 📂 **templates**
            * 📄 [`index.html`](./Lecture/Source%20Code/src9/hello5/templates/index.html)
        * 📂 **hello6**
          * 📄 [`app.py`](./Lecture/Source%20Code/src9/hello6/app.py)
          * 📄 [`requirements.txt`](./Lecture/Source%20Code/src9/hello6/requirements.txt)
          * 📂 **templates**
            * 📄 [`greet.html`](./Lecture/Source%20Code/src9/hello6/templates/greet.html)
            * 📄 [`index.html`](./Lecture/Source%20Code/src9/hello6/templates/index.html)
        * 📂 **hello7**
          * 📄 [`app.py`](./Lecture/Source%20Code/src9/hello7/app.py)
          * 📄 [`requirements.txt`](./Lecture/Source%20Code/src9/hello7/requirements.txt)
          * 📂 **templates**
            * 📄 [`greet.html`](./Lecture/Source%20Code/src9/hello7/templates/greet.html)
            * 📄 [`index.html`](./Lecture/Source%20Code/src9/hello7/templates/index.html)
            * 📄 [`layout.html`](./Lecture/Source%20Code/src9/hello7/templates/layout.html)
        * 📂 **hello8**
          * 📄 [`app.py`](./Lecture/Source%20Code/src9/hello8/app.py)
          * 📄 [`requirements.txt`](./Lecture/Source%20Code/src9/hello8/requirements.txt)
          * 📂 **templates**
            * 📄 [`greet.html`](./Lecture/Source%20Code/src9/hello8/templates/greet.html)
            * 📄 [`index.html`](./Lecture/Source%20Code/src9/hello8/templates/index.html)
            * 📄 [`layout.html`](./Lecture/Source%20Code/src9/hello8/templates/layout.html)
        * 📂 **hello9**
          * 📄 [`app.py`](./Lecture/Source%20Code/src9/hello9/app.py)
          * 📄 [`requirements.txt`](./Lecture/Source%20Code/src9/hello9/requirements.txt)
          * 📂 **templates**
            * 📄 [`greet.html`](./Lecture/Source%20Code/src9/hello9/templates/greet.html)
            * 📄 [`index.html`](./Lecture/Source%20Code/src9/hello9/templates/index.html)
            * 📄 [`layout.html`](./Lecture/Source%20Code/src9/hello9/templates/layout.html)
        * 📂 **login**
          * 📄 [`app.py`](./Lecture/Source%20Code/src9/login/app.py)
          * 📄 [`requirements.txt`](./Lecture/Source%20Code/src9/login/requirements.txt)
          * 📂 **templates**
            * 📄 [`index.html`](./Lecture/Source%20Code/src9/login/templates/index.html)
            * 📄 [`layout.html`](./Lecture/Source%20Code/src9/login/templates/layout.html)
            * 📄 [`login.html`](./Lecture/Source%20Code/src9/login/templates/login.html)
        * 📂 **shows0**
          * 📄 [`app.py`](./Lecture/Source%20Code/src9/shows0/app.py)
          * 📄 [`LICENSE`](./Lecture/Source%20Code/src9/shows0/LICENSE)
          * 📄 [`requirements.txt`](./Lecture/Source%20Code/src9/shows0/requirements.txt)
          * 📄 [`shows.db`](./Lecture/Source%20Code/src9/shows0/shows.db)
          * 📂 **templates**
            * 📄 [`index.html`](./Lecture/Source%20Code/src9/shows0/templates/index.html)
            * 📄 [`layout.html`](./Lecture/Source%20Code/src9/shows0/templates/layout.html)
            * 📄 [`search.html`](./Lecture/Source%20Code/src9/shows0/templates/search.html)
        * 📂 **shows1**
          * 📄 [`app.py`](./Lecture/Source%20Code/src9/shows1/app.py)
          * 📄 [`LICENSE`](./Lecture/Source%20Code/src9/shows1/LICENSE)
          * 📄 [`requirements.txt`](./Lecture/Source%20Code/src9/shows1/requirements.txt)
          * 📄 [`shows.db`](./Lecture/Source%20Code/src9/shows1/shows.db)
          * 📂 **templates**
            * 📄 [`index.html`](./Lecture/Source%20Code/src9/shows1/templates/index.html)
            * 📄 [`layout.html`](./Lecture/Source%20Code/src9/shows1/templates/layout.html)
            * 📄 [`search.html`](./Lecture/Source%20Code/src9/shows1/templates/search.html)
        * 📂 **shows2**
          * 📄 [`app.py`](./Lecture/Source%20Code/src9/shows2/app.py)
          * 📄 [`LICENSE`](./Lecture/Source%20Code/src9/shows2/LICENSE)
          * 📄 [`requirements.txt`](./Lecture/Source%20Code/src9/shows2/requirements.txt)
          * 📄 [`shows.db`](./Lecture/Source%20Code/src9/shows2/shows.db)
          * 📂 **templates**
            * 📄 [`index.html`](./Lecture/Source%20Code/src9/shows2/templates/index.html)
            * 📄 [`search.html`](./Lecture/Source%20Code/src9/shows2/templates/search.html)
        * 📂 **shows3**
          * 📄 [`app.py`](./Lecture/Source%20Code/src9/shows3/app.py)
          * 📄 [`LICENSE`](./Lecture/Source%20Code/src9/shows3/LICENSE)
          * 📄 [`requirements.txt`](./Lecture/Source%20Code/src9/shows3/requirements.txt)
          * 📄 [`shows.db`](./Lecture/Source%20Code/src9/shows3/shows.db)
          * 📂 **templates**
            * 📄 [`index.html`](./Lecture/Source%20Code/src9/shows3/templates/index.html)
        * 📂 **store**
          * 📄 [`app.py`](./Lecture/Source%20Code/src9/store/app.py)
          * 📄 [`requirements.txt`](./Lecture/Source%20Code/src9/store/requirements.txt)
          * 📄 [`store.db`](./Lecture/Source%20Code/src9/store/store.db)
          * 📂 **templates**
            * 📄 [`books.html`](./Lecture/Source%20Code/src9/store/templates/books.html)
            * 📄 [`cart.html`](./Lecture/Source%20Code/src9/store/templates/cart.html)
            * 📄 [`layout.html`](./Lecture/Source%20Code/src9/store/templates/layout.html)
      * 📄 [`src9.pdf`](./Lecture/Source%20Code/src9.pdf)
  * 📂 **Problem Set 9**
    * 📂 **birthdays**
      * 📄 [`app.py`](./Problem%20Set%209/birthdays/app.py)
      * 📄 [`birthdays.db`](./Problem%20Set%209/birthdays/birthdays.db)
      * 📂 **static**
        * 📄 [`styles.css`](./Problem%20Set%209/birthdays/static/styles.css)
      * 📂 **templates**
        * 📄 [`index.html`](./Problem%20Set%209/birthdays/templates/index.html)
    * 📂 **finance**
      * 📄 [`app.py`](./Problem%20Set%209/finance/app.py)
      * 📄 [`finance.db`](./Problem%20Set%209/finance/finance.db)
      * 📂 **flask_session**
        * 📄 [`2029240f6d1128be89ddc32729463129`](./Problem%20Set%209/finance/flask_session/2029240f6d1128be89ddc32729463129)
        * 📄 [`774bc4143517efa773d4017d40eef650`](./Problem%20Set%209/finance/flask_session/774bc4143517efa773d4017d40eef650)
      * 📄 [`helpers.py`](./Problem%20Set%209/finance/helpers.py)
      * 📄 [`requirements.txt`](./Problem%20Set%209/finance/requirements.txt)
      * 📂 **static**
        * 📄 [`favicon.ico`](./Problem%20Set%209/finance/static/favicon.ico)
        * 📄 [`I_heart_validator.png`](./Problem%20Set%209/finance/static/I_heart_validator.png)
        * 📄 [`styles.css`](./Problem%20Set%209/finance/static/styles.css)
      * 📂 **templates**
        * 📄 [`apology.html`](./Problem%20Set%209/finance/templates/apology.html)
        * 📄 [`buy.html`](./Problem%20Set%209/finance/templates/buy.html)
        * 📄 [`history.html`](./Problem%20Set%209/finance/templates/history.html)
        * 📄 [`index.html`](./Problem%20Set%209/finance/templates/index.html)
        * 📄 [`layout.html`](./Problem%20Set%209/finance/templates/layout.html)
        * 📄 [`login.html`](./Problem%20Set%209/finance/templates/login.html)
        * 📄 [`quote.html`](./Problem%20Set%209/finance/templates/quote.html)
        * 📄 [`register.html`](./Problem%20Set%209/finance/templates/register.html)
        * 📄 [`sell.html`](./Problem%20Set%209/finance/templates/sell.html)
  * 📂 **Section**
    * 📂 **Resources**
      * 📄 [`section9.pdf`](./Section/Resources/section9.pdf)
    * 📂 **Source Code**
      * 📂 **birthdays**
        * 📄 [`app.py`](./Section/Source%20Code/birthdays/app.py)
        * 📄 [`birthdays.db`](./Section/Source%20Code/birthdays/birthdays.db)
        * 📂 **static**
          * 📄 [`styles.css`](./Section/Source%20Code/birthdays/static/styles.css)
        * 📂 **templates**
          * 📄 [`index.html`](./Section/Source%20Code/birthdays/templates/index.html)

## 🎥 Video Resources

### Main Lecture

[![Lecture 9](https://img.youtube.com/vi/am7POvSZ4GE/0.jpg)](https://youtu.be/am7POvSZ4GE)

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
[← Return to Course Index](../README.md)
