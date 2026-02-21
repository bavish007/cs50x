# Week 7 SQL

## 🎯 Overview

Week 7 introduces the transition from memory and pointers to data management and databases. The focus shifts from C to Python and SQL, exploring how to store, query, and manipulate data efficiently.

**Key Learning Outcomes:**

1. **Flat-File vs. Relational Databases:** Understanding the limitations of flat-file systems (like CSVs) and the robustness of relational databases (SQLite) for handling complex data relationships.
2. **SQL Mastery:** Learning the Structured Query Language (SQL) to perform CRUD operations (`CREATE`, `READ` / `SELECT`, `UPDATE`, `DELETE`) and advanced queries using `JOIN`, `indexes`, and nested queries.
3. **Python Integration:** Integrating SQL databases with Python code using the CS50 Library (`cs50.SQL`) to build dynamic applications that sanitize inputs and prevent race conditions.

## 📚 Documentation & Resources

| Document | Type | Location |
| :--- | :---: | :--- |
| **Notes** | Markdown | [Lecture/Notes.md](./Lecture/Notes.md) |
| **Lecture 7 Slides** | PPTX | [Lecture/Resources/CS50%202025%20-%20Lecture%207%20-%20SQL.pptx](./Lecture/Resources/CS50%202025%20-%20Lecture%207%20-%20SQL.pptx) |
| **Lecture 7 PDF** | PDF | [Lecture/Resources/lecture7.pdf](./Lecture/Resources/lecture7.pdf) |
| **SQL Cheat Sheet** | PDF | [Lecture/Resources/sql.pdf](./Lecture/Resources/sql.pdf) |
| **Source Code Guide** | PDF | [Lecture/Source%20Code/src7.pdf](./Lecture/Source%20Code/src7.pdf) |
| **Section 7 Notes** | PDF | [Section/Resources/section7.pdf](./Section/Resources/section7.pdf) |

## 🗂️ Complete File Index

<details><summary><b>📂 View Source Files</b></summary>

| File | Type | Link |
| :--- | :---: | :--- |
| 📄 `Notes.md` | .md | [View](./Lecture/Notes.md) |
| 📂 **Lecture / Source Code / src7 / favorites** | Folder | [View](./Lecture/Source%20Code/src7/favorites) |
| 📄 `favorites.csv` | .csv | [View](./Lecture/Source%20Code/src7/favorites/favorites.csv) |
| 📄 `favorites0.py` | .py | [View](./Lecture/Source%20Code/src7/favorites/favorites0.py) |
| 📄 `favorites1.py` | .py | [View](./Lecture/Source%20Code/src7/favorites/favorites1.py) |
| 📄 `favorites2.py` | .py | [View](./Lecture/Source%20Code/src7/favorites/favorites2.py) |
| 📄 `favorites3.py` | .py | [View](./Lecture/Source%20Code/src7/favorites/favorites3.py) |
| 📄 `favorites4.py` | .py | [View](./Lecture/Source%20Code/src7/favorites/favorites4.py) |
| 📄 `favorites5.py` | .py | [View](./Lecture/Source%20Code/src7/favorites/favorites5.py) |
| 📄 `favorites6.py` | .py | [View](./Lecture/Source%20Code/src7/favorites/favorites6.py) |
| 📄 `favorites7.py` | .py | [View](./Lecture/Source%20Code/src7/favorites/favorites7.py) |
| 📄 `favorites8.py` | .py | [View](./Lecture/Source%20Code/src7/favorites/favorites8.py) |
| 📄 `favorites9.py` | .py | [View](./Lecture/Source%20Code/src7/favorites/favorites9.py) |
| 📄 `favorites10.py` | .py | [View](./Lecture/Source%20Code/src7/favorites/favorites10.py) |
| 📂 **Lecture / Source Code / src7 / imdb** | Folder | [View](./Lecture/Source%20Code/src7/imdb) |
| 📄 `LICENSE` | — | [View](./Lecture/Source%20Code/src7/imdb/LICENSE) |
| 📄 `shows.db` | .db | [View](./Lecture/Source%20Code/src7/imdb/shows.db) |
| 📂 **Problem Set 7 / fiftyville** | Folder | [View](./Problem%20Set%207/fiftyville) |
| 📄 `answers.txt` | .txt | [View](./Problem%20Set%207/fiftyville/answers.txt) |
| 📄 `fiftyville.db` | .db | [View](./Problem%20Set%207/fiftyville/fiftyville.db) |
| 📄 `log.sql` | .sql | [View](./Problem%20Set%207/fiftyville/log.sql) |
| 📂 **Problem Set 7 / movies** | Folder | [View](./Problem%20Set%207/movies) |
| 📄 `1.sql` | .sql | [View](./Problem%20Set%207/movies/1.sql) |
| 📄 `2.sql` | .sql | [View](./Problem%20Set%207/movies/2.sql) |
| 📄 `3.sql` | .sql | [View](./Problem%20Set%207/movies/3.sql) |
| 📄 `4.sql` | .sql | [View](./Problem%20Set%207/movies/4.sql) |
| 📄 `5.sql` | .sql | [View](./Problem%20Set%207/movies/5.sql) |
| 📄 `6.sql` | .sql | [View](./Problem%20Set%207/movies/6.sql) |
| 📄 `7.sql` | .sql | [View](./Problem%20Set%207/movies/7.sql) |
| 📄 `8.sql` | .sql | [View](./Problem%20Set%207/movies/8.sql) |
| 📄 `9.sql` | .sql | [View](./Problem%20Set%207/movies/9.sql) |
| 📄 `10.sql` | .sql | [View](./Problem%20Set%207/movies/10.sql) |
| 📄 `11.sql` | .sql | [View](./Problem%20Set%207/movies/11.sql) |
| 📄 `12.sql` | .sql | [View](./Problem%20Set%207/movies/12.sql) |
| 📄 `13.sql` | .sql | [View](./Problem%20Set%207/movies/13.sql) |
| 📄 `LICENSE` | — | [View](./Problem%20Set%207/movies/LICENSE) |
| 📄 `gitignore` | — | [View](./Problem%20Set%207/movies/gitignore) |
| 📂 **Problem Set 7 / songs** | Folder | [View](./Problem%20Set%207/songs) |
| 📄 `1.sql` | .sql | [View](./Problem%20Set%207/songs/1.sql) |
| 📄 `2.sql` | .sql | [View](./Problem%20Set%207/songs/2.sql) |
| 📄 `3.sql` | .sql | [View](./Problem%20Set%207/songs/3.sql) |
| 📄 `4.sql` | .sql | [View](./Problem%20Set%207/songs/4.sql) |
| 📄 `5.sql` | .sql | [View](./Problem%20Set%207/songs/5.sql) |
| 📄 `6.sql` | .sql | [View](./Problem%20Set%207/songs/6.sql) |
| 📄 `7.sql` | .sql | [View](./Problem%20Set%207/songs/7.sql) |
| 📄 `8.sql` | .sql | [View](./Problem%20Set%207/songs/8.sql) |
| 📄 `answers.txt` | .txt | [View](./Problem%20Set%207/songs/answers.txt) |
| 📄 `songs.db` | .db | [View](./Problem%20Set%207/songs/songs.db) |

</details>

## 🎥 Video Resources

### Main Lecture

<div align="center">

[![Lecture 7](https://img.youtube.com/vi/oqRU2So6Z2Y/0.jpg)](https://youtu.be/oqRU2So6Z2Y)

</div>

### 🧠 Concept Clips

* [SQL](https://youtu.be/AywtnUjQ6X4)

## 🛠️ Problem Sets & Labs

### 🕵️‍♀️ Fiftyville

A mystery solving challenge where you assume the role of a data detective. You are given a database of crime reports, airport logs, ATM transactions, and phone calls. Your goal is to write SQL queries in `log.sql` to identify the thief, the accomplice, and the escape city.

### 🎬 Movies

A set of SQL problems based on a subset of the IMDb database. You write queries to answer specific questions about movies, directors, and stars (e.g., "List all movies released in 2008").

### 🎵 Songs

A set of SQL problems exploring a database of songs and artists from Spotify. You write queries to find information like the names of songs, danceability scores, and artist details.

---

<div align="center">
  <br />
  <a href="../README.md">
    <img src="https://img.shields.io/badge/Return_to_Master_Index-181717?style=for-the-badge&logo=github&logoColor=white" alt="Back to Master Index" />
  </a>
</div>
