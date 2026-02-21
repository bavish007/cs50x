# Lecture 7

## Table of Contents

* [Welcome!](#welcome)
* [Flat-File Database](#flat-file-database)
* [Relational Databases](#relational-databases)
* [SELECT](#select)
* [INSERT](#insert)
* [DELETE](#delete)
* [UPDATE](#update)
* [IMDb](#imdb)
* [JOINs](#joins)
* [Indexes](#indexes)
* [Using SQL in Python](#using-sql-in-python)
* [Race Conditions](#race-conditions)
* [SQL Injection Attacks](#sql-injection-attacks)
* [Summing Up](#summing-up)

## Welcome

In previous weeks, I was introduced to Python, a high-level programming language that utilized the same building blocks I learned in C. However, I introduced this new language not for the purpose of learning “just another language.” Instead, I do so because some tools are better for some jobs and not so great for others!

This week, I will be continuing with more syntax related to Python.

Further, I will be integrating this knowledge with data.

Finally, I will be discussing **SQL** or **Structured Query Language**, a domain-specific way by which I can interact with and modify data.

Overall, one of the goals of this course is to learn to program generally – not simply how to program in the languages described in this course.

## Flat-File Database

As I have likely seen before, data can often be described in patterns of columns and rows.

Spreadsheets like those created in Microsoft Excel and Google Sheets can be outputted to a `csv` or **comma-separated values** file.

If I look at a `csv` file, I’ll notice that the file is flat in that all of my data is stored in a single table represented by a text file. We call this form of data a **flat-file database**.

All data is stored row by row. Each column is separated by a comma or another value.

Python comes with native support for `csv` files.

First, I downloaded `favorites.csv` and uploaded it to my file explorer inside cs50.dev. Second, examining this data, I noticed that the first row is special in that it defines each column. Then, each record is stored row by row.

In my terminal window, I typed `code favorites.py` and wrote code as follows:

```python
# Prints all favorites in CSV using csv.reader

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create reader
    reader = csv.reader(file)

    # Skip header row
    next(reader)

    # Iterate over CSV file, printing each favorite
    for row in reader:
        print(row[1])
```

I noticed that the `csv` library is imported. Further, I created a `reader` that will hold the result of `csv.reader(file)`. The `csv.reader` function reads each row from the file, and in my code, I store the results in `reader`. `print(row[1])`, therefore, will print the language from the `favorites.csv` file.

I can improve my code as follows:

```python
# Stores favorite in a variable

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create reader
    reader = csv.reader(file)

    # Skip header row
    next(reader)

    # Iterate over CSV file, printing each favorite
    for row in reader:
        favorite = row[1]
        print(favorite)
```

I noticed that `favorite` is stored and then printed. Also, I use the `next` function to skip to the next line of my reader.

One of the disadvantages of the above approach is that I am trusting that `row[1]` is always the favorite. However, what would happen if the columns had been moved around?

I can fix this potential issue. Python also allows me to index by the keys of a list. I modified my code as follows:

```python
# Prints all favorites in CSV using csv.DictReader

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Iterate over CSV file, printing each favorite
    for row in reader:
        favorite = row["language"]
        print(favorite)
```

I noticed that this example directly utilizes the `language` key in the print statement. `favorite` is assigned the value of `row["language"]`.

This could be further simplified to:

```python
# Prints all favorites in CSV using csv.DictReader

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Iterate over CSV file, printing each favorite
    for row in reader:
        print(row["language"])
```

To count the number of favorite languages expressed in the `csv` file, I can do the following:

```python
# Counts favorites using variables

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Counts
    scratch, c, python = 0, 0, 0

    # Iterate over CSV file, counting favorites
    for row in reader:
        favorite = row["language"]
        if favorite == "Scratch":
            scratch += 1
        elif favorite == "C":
            c += 1
        elif favorite == "Python":
            python += 1

# Print counts
print(f"Scratch: {scratch}")
print(f"C: {c}")
print(f"Python: {python}")
```

I noticed that each language is counted using `if` statements. Further, I noticed the double equal `==` signs in those `if` statements.

Python allows me to use a dictionary to count the counts of each language. I considered the following improvement upon my code:

```python
# Counts favorites using dictionary

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Counts
    counts = {}

    # Iterate over CSV file, counting favorites
    for row in reader:
        favorite = row["language"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

# Print counts
for favorite in counts:
    print(f"{favorite}: {counts[favorite]}")
```

I noticed that the value in `counts` with the key `favorite` is incremented when it exists already. If it does not exist, I define `counts[favorite]` and set it to 1. Further, the formatted string has been improved to present the `counts[favorite]`.

I can also utilize `try` and `except` to account for potential exceptions:

```python
# Uses try/except instead

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Counts
    counts = {}

    # Iterate over CSV file, counting favorites
    for row in reader:
        favorite = row["language"]
        try:
            counts[favorite] += 1
        except KeyError:
            counts[favorite] = 1

# Print counts
for favorite in counts:
    print(f"{favorite}: {counts[favorite]}")
```

I noticed how the `if` and `else` have been replaced with `try` and `except`.

Python also allows sorting counts. I improved my code as follows:

```python
# Sorts favorites by key

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Counts
    counts = {}

    # Iterate over CSV file, counting favorites
    for row in reader:
        favorite = row["language"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

# Print counts
for favorite in sorted(counts):
    print(f"{favorite}: {counts[favorite]}")
```

I noticed the `sorted(counts)` at the bottom of the code.

If I look at the parameters for the `sorted` function in the Python documentation, I will find it has many built-in parameters. I can leverage some of these built-in parameters as follows:

```python
# Sorts favorites by value using .get

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Counts
    counts = {}

    # Iterate over CSV file, counting favorites
    for row in reader:
        favorite = row["language"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

# Print counts
for favorite in sorted(counts, key=counts.get, reverse=True):
    print(f"{favorite}: {counts[favorite]}")
```

I noticed the arguments passed to `sorted`. The `key` argument allows me to tell Python the method I wish to use to sort items. In this case, `counts.get` is used to sort by the values. `reverse=True` tells `sorted` to sort from largest to smallest.

I can learn more about `sorted` in the Python Documentation.

## Relational Databases

Google, X, and Meta all use **relational databases** to store their information at scale.

Relational databases store data in rows and columns in structures called **tables**.

SQL allows for four types of commands:

* Create
* Read
* Update
* Delete

These four operations are affectionately called **CRUD**.

I can create a database with the SQL syntax `CREATE TABLE table (column type, ...);`. But where do I run this command?

`sqlite3` is a type of SQL database that has the core features required for this course.

I can create a SQL database at the terminal by typing `sqlite3 favorites.db`. Upon being prompted, I will agree that I want to create `favorites.db` by pressing `y`.

I will notice a different prompt as I am now using a program called `sqlite`.

I can put `sqlite` into csv mode by typing `.mode csv`. Then, I can import my data from my csv file by typing `.import favorites.csv favorites`. It seems that nothing has happened!

I can type `.schema` to see the structure of the database.

I can read items from a table using the syntax `SELECT columns FROM table`.

For example, I can type `SELECT * FROM favorites;` which will print every row in `favorites`.

I can get a subset of the data using the command `SELECT language FROM favorites;`.

SQL supports many commands to access data, including:

* `AVG`
* `COUNT`
* `DISTINCT`
* `LOWER`
* `MAX`
* `MIN`
* `UPPER`

For example, I can type `SELECT COUNT(*) FROM favorites;`. Further, I can type `SELECT DISTINCT language FROM favorites;` to get a list of the individual languages within the database. I could even type `SELECT COUNT(DISTINCT language) FROM favorites;` to get a count of those.

SQL offers additional commands I can utilize in my queries:

* `WHERE`       -- adding a Boolean expression to filter my data
* `LIKE`        -- filtering responses more loosely
* `ORDER BY`    -- ordering responses
* `LIMIT`       -- limiting the number of responses
* `GROUP BY`    -- grouping responses together

I noticed that I use `--` to write a comment in SQL.

## SELECT

For example, I can execute `SELECT COUNT(*) FROM favorites WHERE language = 'C';`. A count is presented.

Further, I could type `SELECT COUNT(*) FROM favorites WHERE language = 'C' AND problem = 'Hello, World';`. I noticed how the `AND` is utilized to narrow my results.

Similarly, I could execute `SELECT language, COUNT(*) FROM favorites GROUP BY language;`. This would offer a temporary table that would show the language and count.

I could improve this by typing `SELECT language, COUNT(*) FROM favorites GROUP BY language ORDER BY COUNT(*);`. This will order the resulting table by the count.

Likewise, I could execute `SELECT COUNT(*) FROM favorites WHERE language = 'C' AND (problem = 'Hello, World' OR problem = 'Hello, It''s Me');`. I noticed that there are two `'` marks to allow the use of single quotes in a way that does not confuse SQL.

Further, I could execute `SELECT COUNT(*) FROM favorites WHERE language = 'C' AND problem LIKE 'Hello, %';` to find any problems that start with `Hello,` (including a space).

I can order the output as follows: `SELECT language, COUNT(*) FROM favorites GROUP BY language ORDER BY COUNT(*) DESC;`.

I can even create aliases, like variables in my queries: `SELECT language, COUNT(*) AS n FROM favorites GROUP BY language ORDER BY n DESC;`.

Finally, I can limit my output to 1 or more values: `SELECT language, COUNT(*) AS n FROM favorites GROUP BY language ORDER BY n DESC LIMIT 1;`.

I noticed, by convention, SQL keywords are often typed in caps.

## INSERT

I can also **INSERT** into a SQL database utilizing the form `INSERT INTO table (column...) VALUES(value, ...);`.

I can execute `INSERT INTO favorites (language, problem) VALUES ('SQL', 'Fiftyville');`.

I can verify the addition of this favorite by executing `SELECT * FROM favorites;`.

## DELETE

**DELETE** allows me to delete parts of my data. For example, I could `DELETE FROM favorites WHERE Timestamp IS NULL;`. This deletes any record where the Timestamp is NULL.

## UPDATE

I can also utilize the **UPDATE** command to update my data.

For example, I can execute `UPDATE favorites SET language = 'SQL', problem = 'Fiftyville';`. This will result in updating all the rows.

I noticed that these queries have immense power. Accordingly, in the real-world setting, I should consider who has permissions to execute certain commands and if I have backups available!

## IMDb

I can imagine a database that I might want to create to catalog various TV shows. I could create a spreadsheet with columns like title, star, star, star, star, and more stars. A problem with this approach is that it has a lot of wasted space. Some shows may have one star. Others may have dozens.

I could separate my database into multiple sheets. I could have a `shows` sheet, a `stars` sheet, and a `people` sheet. On the `people` sheet, each person could have a unique `id`. On the `shows` sheet, each show could have a unique `id` too. On a third sheet called `stars` I could relate people to shows by having a `show_id` and `person_id`. While this is an improvement, this is not an ideal database.

IMDb offers a database of people, shows, writers, stars, genres, and ratings. Each of these tables is related to one another as follows:

![IMDb](https://cs50.harvard.edu/x/2024/notes/7/imdb.png)

After downloading `shows.db`, I can execute `sqlite3 shows.db` in my terminal window.

Let’s zero in on the relationship between two tables within the database called `shows` and `ratings`. The relationship between these two tables can be illustrated as follows:

![Shows and Ratings](https://cs50.harvard.edu/x/2024/notes/7/shows_ratings.png)

To illustrate the relationship between these tables, I could execute the following command: `SELECT * FROM ratings LIMIT 10;`. Examining the output, I could execute `SELECT * FROM shows LIMIT 10;`.

Examining `shows` and `ratings`, I can see these have a **one-to-one** relationship: One show has one rating.

To understand the database, upon executing `.schema` I will find not only each of the tables but the individual fields inside each of these tables.

More specifically, I could execute `.schema shows` to understand the fields inside `shows`. I can also execute `.schema ratings` to see the fields inside `ratings`.

A reference to the show’s `id` exists in all tables. In the `shows` table, it is simply called `id`. This common field among all the tables is called a **key**. **Primary keys** are used to identify a unique record in a table. **Foreign keys** are used to build relationships between tables by pointing to the primary key in another table. I can see in the schema of `ratings` that `show_id` is a foreign key that references `id` in `shows`.

By storing data in a relational database, as above, data can be more efficiently stored.

In sqlite, we have five data types, including:

* `BLOB`       -- binary large objects that are groups of ones and zeros
* `INTEGER`    -- an integer
* `NUMERIC`    -- for numbers that are formatted specially like dates
* `REAL`       -- like a float
* `TEXT`       -- for strings and the like

Additionally, columns can be set to add special constraints:

* `NOT NULL`
* `UNIQUE`

I can further play with this data to understand these relationships. Execute `SELECT * FROM ratings;`. There are a lot of ratings!

I can further limit this data down by executing `SELECT show_id FROM ratings WHERE rating >= 6.0 LIMIT 10;`. From this query, I can see that there are 10 shows presented. However, I don’t know what show each `show_id` represents.

I can discover what shows these are by executing `SELECT * FROM shows WHERE id = 626124;`

I can refine my query to be more efficient by executing:

```sql
SELECT title
FROM shows
WHERE id IN (
    SELECT show_id
    FROM ratings
    WHERE rating >= 6.0
    LIMIT 10
);
```

I noticed that this query nests together two queries. An **inner query** is used by an **outer query**.

## JOINs

I are pulling data from `shows` and `ratings`. I noticed how both `shows` and `ratings` have an `id` in common.

How could I combine tables temporarily? Tables could be joined together using the `JOIN` command.

Execute the following command:

```sql
SELECT * FROM shows
  JOIN ratings ON shows.id = ratings.show_id
  WHERE rating >= 6.0
  LIMIT 10;
```

I noticed this results in a wider table than I have previously seen.

Where the previous queries have illustrated the one-to-one relationship between these keys, let’s examine some **one-to-many** relationships. Focusing on the `genres` table, execute the following:

```sql
SELECT * FROM genres
LIMIT 10;
```

I noticed how this provides me a sense of the raw data. I might notice that one show has three values. This is a one-to-many relationship.

I can learn more about the `genres` table by typing `.schema genres`.

Execute the following command to learn more about the various comedies in the database:

```sql
SELECT title FROM shows
WHERE id IN (
  SELECT show_id FROM genres
  WHERE genre = 'Comedy'
  LIMIT 10
);
```

I noticed how this produces a list of comedies, including *Catweazle*.

I can learn more about *Catweazle* by joining various tables:

```sql
SELECT * FROM shows
JOIN genres
ON shows.id = genres.show_id
WHERE id = 63881;
```

I noticed that this results in a temporary table. It is fine to have a duplicate table. Further, I noticed that *Catweazle* (one title) is assigned many genres, including adventure, comedy, and family.

In contrast to one-to-one and one-to-many relationships, there are **many-to-many** relationships. For example, many people could appear in many shows!

I can learn more about the show *The Office* and the actors in that show by executing the following command:

```sql
SELECT name FROM people WHERE id IN 
    (SELECT person_id FROM stars WHERE show_id = 
        (SELECT id FROM shows WHERE title = 'The Office' AND year = 2005));
```

I noticed that this results in a table that includes the names of various stars through nested queries.

I can find all the shows in which Steve Carell starred:

```sql
SELECT title FROM shows WHERE id IN 
    (SELECT show_id FROM stars WHERE person_id = 
        (SELECT id FROM people WHERE name = 'Steve Carell'));
```

This results in a list of titles of shows wherein Steve Carell starred.

This could be expressed as a `JOIN` as:

```sql
SELECT title FROM shows
JOIN stars ON shows.id = stars.show_id
JOIN people ON stars.person_id = people.id
WHERE name = 'Steve Carell';
```

This could also be expressed in this way:

```sql
SELECT title FROM shows, stars, people 
WHERE shows.id = stars.show_id
AND people.id = stars.person_id
AND name = 'Steve Carell';
```

The wildcard `%` operator can be used to find all people whose names start with Steve C by employing the following syntax: `SELECT * FROM people WHERE name LIKE 'Steve C%';`.

## Indexes

While relational databases have the ability to be faster and more robust than utilizing a CSV file, data can be optimized within a table using **indexes**.

Indexes can be utilized to speed up my queries.

I can track the speed of my queries by executing `.timer on` in `sqlite3`.

To understand how indexes can speed up my queries, run the following: `SELECT * FROM shows WHERE title = 'The Office';`. Notice the time that displays after the query executes.

Then, I can create an index with the syntax `CREATE INDEX title_index ON shows (title);`. This tells `sqlite3` to create an index and perform some special under-the-hood optimization relating to this column `title`.

This will create a data structure called a **B Tree**, a data structure that looks similar to a binary tree. However, unlike a binary tree, there can be more than two child nodes.

![B Tree](https://cs50.harvard.edu/x/2024/notes/7/b_tree.png)

Further, I can create indexes as follows:

```sql
CREATE INDEX name_index ON people (name);
CREATE INDEX person_index ON stars (person_id);
```

Run the query and I will notice that the query runs much more quickly!

```sql
SELECT title FROM shows WHERE id IN 
    (SELECT show_id FROM stars WHERE person_id = 
        (SELECT id FROM people WHERE name = 'Steve Carell'));
```

Unfortunately, indexing all columns would result in utilizing more storage space. Therefore, there is a tradeoff for enhanced speed.

## Using SQL in Python

To assist in working with SQL in this course, the CS50 Library can be utilized as follows in my code:

```python
from cs50 import SQL
```

Similar to previous uses of the CS50 Library, this library will assist with the complicated steps of utilizing SQL within my Python code.

I can read more about the CS50 Library’s SQL functionality in the documentation.

Using my new knowledge, I can now leverage Python alongside SQL.

I modified my code for `favorites.py` as follows:

```python
# Searches database for popularity of a problem

from cs50 import SQL

# Open database
db = SQL("sqlite:///favorites.db")

# Prompt user for favorite
favorite = input("Favorite: ")

# Search for title
rows = db.execute("SELECT COUNT(*) AS n FROM favorites WHERE problem = ?", favorite)

# Get first (and only) row
row = rows[0]

# Print popularity
print(row["n"])
```

I noticed that `db = SQL("sqlite:///favorites.db")` provides Python the location of the database file. Then, the line that begins with `rows` executes SQL commands utilizing `db.execute`. Indeed, this command passes the syntax within the quotation marks to the `db.execute` function. I can issue any SQL command using this syntax. Further, I noticed that `rows` is returned as a list of dictionaries. In this case, there is only one result, one row, returned to the `rows` list as a dictionary.

## Race Conditions

Utilization of SQL can sometimes result in some problems.

I can imagine a case where multiple users could be accessing the same database and executing commands at the same time.

This could result in glitches where code is interrupted by other people’s actions. This could result in a loss of data.
Built-in SQL features such as `BEGIN TRANSACTION`, `COMMIT`, and `ROLLBACK` help avoid some of these race condition problems.

## SQL Injection Attacks

Now, still considering the code above, I might be wondering what the `?` question marks do above. One of the problems that can arise in real-world applications of SQL is what is called an **injection attack**. An injection attack is where a malicious actor could input malicious SQL code.

For example, I considered a login screen as follows:

![Login](https://cs50.harvard.edu/x/2024/notes/7/login.png)

Without the proper protections in my own code, a bad actor could run malicious code. I considered the following:

```python
rows = db.execute("SELECT COUNT(*) FROM users WHERE username = ? AND password = ?", username, password)
```

I noticed that because the `?` is in place, validation can be run on `username` and `password` before they are blindly accepted by the query.

Never blindly trust the user’s input.

Utilizing the CS50 Library, the library will sanitize and remove any potentially malicious characters.

## Summing Up

In this lesson, I learned more syntax related to Python. Further, I learned how to integrate this knowledge with data in the form of flat-file and relational databases. Finally, I learned about SQL. Specifically, I discussed…

* Flat-file databases
* Relational databases
* SQL commands such as SELECT, CREATE, INSERT, DELETE, and UPDATE.
* Primary and foreign keys
* JOINs
* Indexes
* Using SQL in Python
* Race conditions
* SQL injection attacks

This was CS50 Week 7 SQL.
