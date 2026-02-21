# Lecture 6

## Table of Contents

* [Welcome!](#welcome)
* [Hello Python!](#hello-python)
* [Speller](#speller)
* [Filter](#filter)
* [Functions](#functions)
* [Libraries, Modules, and Packages](#libraries-modules-and-packages)
* [Strings](#strings)
* [Positional Parameters and Named Parameters](#positional-parameters-and-named-parameters)
* [Variables](#variables)
* [Types](#types)
* [Calculator](#calculator)
* [Conditionals](#conditionals)
* [Object-Oriented Programming](#object-oriented-programming)
* [Loops](#loops)
* [Abstraction](#abstraction)
* [Truncation and Floating Point Imprecision](#truncation-and-floating-point-imprecision)
* [Exceptions](#exceptions)
* [Mario](#mario)
* [Lists](#lists)
* [Searching and Dictionaries](#searching-and-dictionaries)
* [Summing Up](#summing-up)

## Welcome

In previous weeks, I was introduced to the fundamental building blocks of programming.

I learned about programming in a lower-level programming language called C.

Today, I am going to work with a higher-level programming language called **Python**.

As I learn this new language, I’m going to find that I am going to be more able to teach myself new programming languages.

## Hello Python

Humans, over the decades, have seen how previous design decisions made in prior programming languages could be improved upon.

Python is a programming language that builds upon what I have already learned in C.

Python additionally has access to a vast number of user-created libraries.

Unlike in C, which is a compiled language, Python is an **interpreted** language, where I need not separately compile my program. Instead, I run my program in the Python Interpreter.

Up until this point, the code has looked like this:

```c
// A program that says hello to the world

#include <stdio.h>

int main(void)
{
    printf("hello, world\n");
}
```

I noticed how this C program is more complex than the Python version below.

Today, I’ll find that the process of writing and compiling code has been simplified.
For example, the above code will be rendered in Python as:

```python
# A program that says hello to the world

print("hello, world")
```

I noticed that the semicolon is gone and that no library is needed. I can run this program in my terminal by typing `python hello.py`.

Python notably can implement what was quite complicated in C with relative simplicity.

Among the goals of this week is to be more comfortable with being uncomfortable not knowing exactly how to solve a problem or correctly, syntactically implement a solution: Searching myself for resources to help me (within the course’s academic honesty policy)!

## Speller

To illustrate this simplicity, I typed `code dictionary.py` in the terminal window and wrote code as follows:

```python
# Words in dictionary
words = set()


def check(word):
    """Return true if word is in dictionary else false"""
    return word.lower() in words


def load(dictionary):
    """Load dictionary into memory, returning true if successful else false"""
    with open(dictionary) as file:
        words.update(file.read().splitlines())
    return True


def size():
    """Returns number of words in dictionary if loaded else 0 if not yet loaded"""
    return len(words)


def unload():
    """Unloads dictionary from memory, returning true if successful else false"""
    return True
```

I noticed that there are four functions above. In the `check` function, if a word is in `words`, it returns `True`. It is so much easier than an implementation in C! Similarly, in the `load` function, the dictionary file is opened. For each line in that file, I add that line to `words`. Using `rstrip`, the trailing new line is removed from the added word. `size` simply returns the `len` or length of `words`. `unload` only needs to return `True` because Python handles memory management on its own.

The above code illustrates why higher-level languages exist: To simplify and allow me to write code more easily.

However, speed is a tradeoff. Because C allows me, the programmer, to make decisions about memory management, it may run faster than Python – depending on my code. While C only runs my lines of code, Python runs all the code that comes under the hood with it when I call Python’s built-in functions.

I can learn more about functions in the Python documentation.

## Filter

To further illustrate this simplicity, I created a new file by typing `code blur.py` in my terminal window and wrote code as follows:

```python
# Blurs an image

from PIL import Image, ImageFilter

# Blur image
before = Image.open("bridge.bmp")
after = before.filter(ImageFilter.BoxBlur(1))
after.save("out.bmp")
```

I noticed that this program imports modules `Image` and `ImageFilter` from a library called `PIL`. This takes an input file and creates an output file.

Further, I can create a new file called `edges.py` as follows:

```python
# Blurs an image

from PIL import Image, ImageFilter

# Find edges
before = Image.open("bridge.bmp")
after = before.filter(ImageFilter.FIND_EDGES)
after.save("out.bmp")
```

I noticed that this code is a small adjustment to my blur code but produces a dramatically different result.

Python allows me to abstract away programming that would be much more complicated within C and other lower-level programming languages.

One of the trade-offs of using Python is an interpreted language, instead of being compiled (as I strictly defined earlier in the course). Accordingly, there is some (usually very small) slow-down that may not be expected in a compiled program.

## Functions

In C, I may have seen functions as follows:

```c
printf("hello, world\n");
```

In Python, I will see functions as follows:

```python
print("hello, world")
```

## Libraries, Modules, and Packages

As with C, the CS50 library can be utilized within Python.

The following functions will be of particular use:

* `get_float`
* `get_int`
* `get_string`

I can import the cs50 library as follows:

```python
import cs50
```

I also have the option of importing only specific functions from the CS50 library as follows:

```python
from cs50 import get_float, get_int, get_string
```

## Strings

In C, I might remember this code:

```c
// get_string and printf with %s

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string answer = get_string("What's your name? ");
    printf("hello, %s\n", answer);
}
```

I noticed how this C program uses the CS50 library to get user input.

This code is transformed in Python to:

```python
# get_string and print, with concatenation

from cs50 import get_string

answer = get_string("What's your name? ")
print("hello, " + answer)
```

I can write this code by executing `code hello.py` in the terminal window. Then, I can execute this code by running `python hello.py`. I noticed how the `+` sign concatenates `"hello, "` and `answer`.

Similarly, this can be done without concatenation:

```python
# get_string and print, without concatenation

from cs50 import get_string

answer = get_string("What's your name? ")
print("hello,", answer)
```

I noticed that the print statement automatically creates a space between the hello statement and the answer.

Similarly, I could implement the above code as:

```python
# get_string and print, with format strings

from cs50 import get_string

answer  = get_string("What's your name? ")
print(f"hello, {answer}")
```

I noticed how the curly braces allow for the print function to interpolate the answer such that answer appears within. The `f` is required to include the answer properly formatting.

## Positional Parameters and Named Parameters

Functions in C like `fread`, `fwrite`, and `printf` use **positional arguments**, where I provide arguments with commas as separators. I, the programmer, must remember what argument is in which position. These are referred to as positional arguments.

In Python, **named parameters** allow me to provide arguments without regard to positionality.

I can learn more about the parameters of the print function in the documentation.

Accessing that documentation, I may see the following:

```python
print(*objects, sep=' ', end='\n', file=None, flush=False)
```

I noticed that various objects can be provided to print. A separator of a single space is provided that will display when more than one object is given to print. Similarly, a new line is provided at the end of the print statement.

## Variables

Variable declaration is simplified too. In C, I might have `int counter = 0;`. In Python, this same line would read `counter = 0`. I need not declare the type of the variable.

Python favors `counter += 1` to increment by one, losing the ability found in C to type `counter++`.

## Types

Data types in Python do not need to be explicitly declared. For example, I saw how `answer` above is a string, but I did not have to tell the interpreter this was the case: It knew on its own.

In Python, commonly used types include:

* `bool`
* `float`
* `int`
* `str`

I noticed that `long` and `double` are missing. Python will handle what data type should be used for larger and smaller numbers.

Some other data types in Python include:

* `range` sequence of numbers
* `list` sequence of mutable values
* `tuple` sequence of immutable values
* `dict` collection of key-value pairs
* `set` collection of unique values

Each of these data types can be implemented in C, but in Python, they can be implemented more simply.

## Calculator

I might recall `calculator.c` from earlier in the course:

```c
// Addition with int

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for x
    int x = get_int("x: ");

    // Prompt user for y
    int y = get_int("y: ");

    // Perform addition
    printf("%i\n", x + y);
}
```

I noticed this C implementation of a simple calculator.

I can implement a simple calculator just as I did within C. I typed `code calculator.py` into the terminal window and wrote code as follows:

```python
# Addition with int [using get_int]

from cs50 import get_int

# Prompt user for x
x = get_int("x: ")

# Prompt user for y
y = get_int("y: ")

# Perform addition
print(x + y)
```

I noticed how the CS50 library is imported. Then, `x` and `y` are gathered from the user. Finally, the result is printed. I noticed that the `main` function that would have been seen in a C program is gone entirely! While one could utilize a `main` function, it is not required.

It’s possible for one to remove the training wheels of the CS50 library. I modified my code as follows:

```python
# Addition with int [using input]

# Prompt user for x
x = input("x: ")

# Prompt user for y
y = input("y: ")

# Perform addition
print(x + y)
```

I noticed how executing the above code results in strange program behavior. I asked myself, "Why might this be so?"

I may have guessed that the interpreter understood `x` and `y` to be strings. I can fix my code by employing the `int` function as follows:

```python
# Addition with int [using input]

# Prompt user for x
x = int(input("x: "))

# Prompt user for y
y = int(input("y: "))

# Perform addition
print(x + y)
```

I noticed how the input for `x` and `y` is passed to the `int` function, which converts it to an integer. Without converting `x` and `y` to be integers, the characters will concatenate.

## Conditionals

In C, I might remember a program like this:

```c
// Conditionals, Boolean expressions, relational operators

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for integers
    int x = get_int("What's x? ");
    int y = get_int("What's y? ");

    // Compare integers
    if (x < y)
    {
        printf("x is less than y\n");
    }
    else if (x > y)
    {
        printf("x is greater than y\n");
    }
    else
    {
        printf("x is equal to y\n");
    }
}
```

I noticed how conditionals work in C.

In Python, it would appear as follows:

```python
# Conditionals, Boolean expressions, relational operators

from cs50 import get_int

# Prompt user for integers
x = get_int("What's x? ")
y = get_int("What's y? ")

# Compare integers
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
```

I noticed that there are no more curly braces. Instead, indentations are utilized. Second, a colon is utilized in the `if` statement. Further, `elif` replaces `else if`. Parentheses are also no longer required in the `if` and `elif` statements.

Further looking at comparisons, I considered the following code in C:

```c
// Logical operators

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user to agree
    char c = get_char("Do you agree? ");

    // Check whether agreed
    if (c == 'Y' || c == 'y')
    {
        printf("Agreed.\n");
    }
    else
    {
        printf("Not agreed.\n");
    }
}
```

I noticed how logical operators work in C.

The above can be implemented as follows:

```python
# Logical operators

from cs50 import get_string

# Prompt user to agree
s = get_string("Do you agree? ")

# Check whether agreed
if s == "Y" or s == "y":
    print("Agreed.")
else:
    print("Not agreed.")
```

I noticed that the two vertical bars utilized in C is replaced with `or`. Indeed, people often enjoy Python because it is more readable by humans. Also, I noticed that `char` does not exist in Python. Instead, `str`s are utilized.

Another approach to this same code could be as follows using lists:

```python
# Logical operators, using lists

from cs50 import get_string

# Prompt user to agree
s = get_string("Do you agree? ")

# Check whether agreed
if s in ["y", "yes"]:
    print("Agreed.")
else:
    print("Not agreed.")
```

I noticed how I am able to express multiple keywords like `y` and `yes` in a list.

## Object-Oriented Programming

It’s possible to have certain types of values not only have properties or attributes inside of them but have functions as well. In Python, these values are known as **objects**.

In C, I could create a struct where I could associate multiple variables inside a single self-created data type. In Python, I can do this and also include functions in a self-created data type. When a function belongs to a specific object, it is known as a **method**.

For example, `str`s in Python have built-in methods. Therefore, I could modify my code as follows:

```python
# Logical operators, using lists

# Prompt user to agree
s = input("Do you agree? ").lower()

# Check whether agreed
if s in ["y", "yes"]:
    print("Agreed.")
else:
    print("Not agreed.")
```

I noticed how I use `s.lower()` to normalize input, using the built-in `lower` method of `str`s.

Similarly, I may recall how I copied a string in C:

```c
// Capitalizes a copy of a string without memory errors

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    // Get a string
    char *s = get_string("s: ");
    if (s == NULL)
    {
        return 1;
    }

    // Allocate memory for another string
    char *t = malloc(strlen(s) + 1);
    if (t == NULL)
    {
        return 1;
    }

    // Copy string into memory
    strcpy(t, s);

    // Capitalize copy
    if (strlen(t) > 0)
    {
        t[0] = toupper(t[0]);
    }

    // Print strings
    printf("s: %s\n", s);
    printf("t: %s\n", t);

    // Free memory
    free(t);
    return 0;
}
```

I noticed the number of lines of code.

I may implement the above in Python as follows:

```python
# Capitalizes a copy of a string

# Get a string
s = input("s: ")

# Capitalize copy of string
t = s.capitalize()

# Print strings
print(f"s: {s}")
print(f"t: {t}")
```

I noticed how much shorter this program is than its counterpart in C.

In this class, I learned I will only scratch the surface of Python. Therefore, the Python documentation will be of particular importance as I continue.

I can learn more about string methods in the Python documentation.

## Loops

Loops in Python are very similar to C. I may recall the following code in C:

```c
// Demonstrates for loop

#include <stdio.h>

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        printf("meow\n");
    }
}
```

`for` loops can be implemented in Python as follows:

```python
# Better design

for i in range(3):
    print("meow")
```

I noticed that `i` is never explicitly used. However, Python will increment the value of `i`.

Further, a `while` loop could be implemented as follows:

```python
# Demonstrates while loop

i = 0
while i < 3:
    print("meow")
    i += 1
```

To further my understanding of loops and iteration in Python, I created a new file called `uppercase.py` as follows:

```python
# Uppercases string one character at a time

before = input("Before: ")
print("After:  ", end="")
for c in before:
    print(c.upper(), end="")
print()
```

I noticed how `end=""` is used to pass a parameter to the print function that continues the line without a line ending. This code passes one string at a time.

Reading the documentation, I discovered that Python has methods that can be implemented upon the entire string as follows:

```python
# Uppercases string all at once

before = input("Before: ")
after = before.upper()
print(f"After:  {after}")
```

I noticed how `.upper` is applied to the entire string.

## Abstraction

As I hinted at earlier today, I can further improve upon my code using functions and abstracting away various code into functions. I modified my earlier-created `meow.py` code as follows:

```python
# Abstraction

def main():
    for i in range(3):
        meow()

# Meow once
def meow():
    print("meow")


main()
```

I noticed that the `meow` function abstracts away the print statement. Further, I noticed that the `main` function appears at the top of the file. At the bottom of the file, the `main` function is called. By convention, it’s expected that I create a `main` function in Python.

Indeed, I can pass variables between my functions as follows:

```python
# Abstraction with parameterization

def main():
    meow(3)


# Meow some number of times
def meow(n):
    for i in range(n):
        print("meow")


main()
```

I noticed how `meow` now takes a variable `n`. In the `main` function, I can call `meow` and pass a value like 3 to it. Then, `meow` utilizes the value of `n` in the for loop.

Reading the above code, I notice how I, as a C programmer, am able to quite easily make sense of the above code. While some conventions are different, the building blocks I previously learned are very apparent in this new programming language.

## Truncation and Floating Point Imprecision

I recalled that in C, I experienced truncation where one integer is divided by another could result in an imprecise result.

I can see how Python handles such division as follows by modifying my code for `calculator.py`:

```python
# Division with integers, demonstration lack of truncation

# Prompt user for x
x = int(input("x: "))

# Prompt user for y
y = int(input("y: "))

# Divide x by y
z = x / y
print(z)
```

I noticed that executing this code results in a value, but that if I were to see more digits after .333333 I’d see that I am faced with floating-point imprecision. Truncation does not occur.

I can reveal this imprecision by modifying my codes slightly:

```python
# Floating-point imprecision

# Prompt user for x
x = int(input("x: "))

# Prompt user for y
y = int(input("y: "))

# Divide x by y
z = x / y
print(f"{z:.50f}")
```

I noticed that this code reveals the imprecision. Python still faces this issue, just as C does.

## Exceptions

Let’s explore more about exceptions that can occur when I run Python code.

I modified `integer.py` as follows:

```python
# Doesn't handle exception

# Prompt user for an integer
n = int(input("Input: "))
print("Integer")
```

I noticed that inputting the wrong data could result in an error.

I can try to handle and catch potential exceptions by modifying my code as follows:

```python
# Handles exception

# Prompt user for an integer
try:
    n = int(input("Input: "))
    print("Integer.")
except ValueError:
    print("Not integer.")
```

I noticed that the above code repeatedly tries to get the correct type of data, providing additional prompts when needed.

## Mario

I recalled a few weeks ago my challenge of building three blocks on top of one another, like in Mario.

![Blocks](https://cs50.harvard.edu/x/2024/notes/6/blocks.png)

In Python, I can implement something akin to this as follows:

```python
# Prints a column of 3 bricks with a loop

for i in range(3):
    print("#")
```

This prints a column of three bricks.

In C, I had the advantage of a `do-while` loop. However, in Python, it is conventional to utilize a `while` loop, as Python does not have a `do-while` loop. I can write code as follows in a file called `mario.py`:

```python
# Prints a column of n bricks with a loop

from cs50 import get_int

while True:
    n = get_int("Height: ")
    if n > 0:
        break

for i in range(n):
    print("#")
```

I noticed how the `while` loop is used to obtain the height. Once a height greater than zero is inputted, the loop breaks.

I considered the following image:

![Question Blocks](https://cs50.harvard.edu/x/2024/notes/6/question_blocks.png)

In Python, I could implement by modifying my code as follows:

```python
# Prints a row of 4 question marks with a loop

for i in range(4):
    print("?", end="")
print()
```

I noticed that I can override the behavior of the print function to stay on the same line as the previous print.

Similar in spirit to previous iterations, I can further simplify this program:

```python
# Prints a row of 4 question marks without a loop

print("?" * 4)
```

I noticed that I can utilize `*` to multiply the print statement to repeat 4 times.

What about a large block of bricks?

![Grid](https://cs50.harvard.edu/x/2024/notes/6/grid.png)

To implement the above, I can modify my code as follows:

```python
# Prints a 3-by-3 grid of bricks with loops

for i in range(3):
    for j in range(3):
        print("#", end="")
    print()
```

I noticed how one `for` loop exists inside another. The print statement adds a new line at the end of each row of bricks.

I can learn more about the print function in the Python documentation.

## Lists

`list`s are a data structure within Python.

`list`s have built-in methods or functions within them.

For example, I considered the following code:

```python
# Averages three numbers using a list

# Scores
scores = [72, 73, 33]

# Print average
average = sum(scores) / len(scores)
print(f"Average: {average}")
```

I noticed that I can use the built-in `sum` method to calculate the average.

I can even utilize the following syntax to get values from the user:

```python
# Averages three numbers using a list and a loop

from cs50 import get_int

# Get scores
scores = []
for i in range(3):
    score = get_int("Score: ")
    scores.append(score)

# Print average
average = sum(scores) / len(scores)
print(f"Average: {average}")
```

I noticed that this code utilizes the built-in `append` method for lists.

I can learn more about lists in the Python documentation.

I can also learn more about `len` in the Python documentation.

## Searching and Dictionaries

I can also search within a data structure.

I considered a program called `phonebook.py` as follows:

```python
# Implements linear search for names using loop

# A list of names
names = ["Kelly", "David", "John"]

# Ask for name
name = input("Name: ")

# Search for name
for n in names:
    if name == n:
        print("Found")
        break
else:
    print("Not found")
```

I noticed how this implements linear search for each name.

However, I don’t need to iterate through a list. In Python, I can execute linear search as follows:

```python
# Implements linear search for names using `in`

# A list of names
names = ["Kelly", "David", "John"]

# Ask for name
name = input("Name: ")

# Search for name
if name in names:
    print("Found")
else:
    print("Not found")
```

I noticed how `in` is used to implement linear search.

Still, this code could be improved.

I recalled that a **dictionary** or `dict` is a collection of key and value pairs.

I can implement a dictionary in Python as follows:

```python
# Implements a phone book as a list of dictionaries, without a variable

from cs50 import get_string

people = [
    {"name": "Kelly", "number": "+1-617-495-1000"},
    {"name": "David", "number": "+1-617-495-1000"},
    {"name": "John", "number": "+1-949-468-2750"},
]

# Search for name
name = get_string("Name: ")
for person in people:
    if person["name"] == name:
        print(f"Found {person['number']}")
        break
else:
    print("Not found")
```

I noticed that the dictionary is implemented having both `name` and `number` for each entry.

Even better, strictly speaking, I don’t need both a name and a number. I can simplify this code as follows:

```python
# Implements a phone book using a dictionary

from cs50 import get_string

people = {
    "Kelly": "+1-617-495-1000",
    "David": "+1-617-495-1000",
    "John": "+1-949-468-2750",
}

# Search for name
name = get_string("Name: ")
if name in people:
    print(f"Number: {people[name]}")
else:
    print("Not found")
```

I noticed that the dictionary is implemented using curly braces. Then, the statement `if name in people` searches to see if the name is in the `people` dictionary. Further, I noticed how, in the `print` statement, I can index into the `people` dictionary using the value of `name`. Very useful!

## Summing Up

In this lesson, I learned about the building blocks of programming in Python. Specifically, I delved into…

* Functions
* Types, Variables
* Conditionals
* Loops
* Abstraction
* Objects
* Searching and Dictionaries
* Command-Line Arguments
* Exit Status
* CSV Files
* Third-Party Libraries

This was CS50 Week 6 Python.
