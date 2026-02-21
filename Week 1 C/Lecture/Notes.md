# Lecture 1

## Table of Contents

* [Welcome!](#welcome)
* [Source Code](#source-code)
* [Visual Studio Code for CS50](#visual-studio-code-for-cs50)
* [Hello World](#hello-world)
* [From Scratch to C](#from-scratch-to-c)
* [Header Files and CS50 Manual Pages](#header-files-and-cs50-manual-pages)
* [Hello, You](#hello-you)
* [Linux](#linux)
* [Conditionals](#conditionals)
* [Types](#types)
* [Format Codes](#format-codes)
* [Variables](#variables)
* [compare.c](#comparec)
* [agree.c](#agreec)
* [Loops and meow.c](#loops-and-meowc)
* [Functions](#functions)
* [Correctness, Design, Style](#correctness-design-style)
* [Mario](#mario)
* [Operators](#operators)
* [Summing Up](#summing-up)

## Welcome

In my previous session, I learned about Scratch, a visual programming language.

I learned that learning computer science concepts can be quite challenging. Indeed, it can feel like I am drinking from a firehose. I remembered: What is ultimately important is the gains I experience over these coming weeks and months through my hard work and study in this course.

Indeed, I found that all the essential programming concepts presented in Scratch will be utilized as I learn how to program any programming language. Functions, conditionals, loops, and variables found in Scratch are fundamental building blocks that I will find in any programming language.

## Source Code

I recalled that machines only understand binary. Where humans write **source code**, a list of instructions for the computer that is human readable, machines only understand what I can now call **machine code**. This machine code is a pattern of ones and zeros that produces a desired effect.

It turns out that I can convert source code into machine code using a very special piece of software called a **compiler**. Today, I was introduced to a compiler that will allow me to convert source code in the programming language **C** into machine code.

![Source Code](https://cs50.harvard.edu/x/2024/notes/1/source_code.png)

![Compiler](https://cs50.harvard.edu/x/2024/notes/1/compiler.png)

![Machine Code](https://cs50.harvard.edu/x/2024/notes/1/machine_code.png)

Today, in addition to learning how to program, I learned how to write good code.

## Visual Studio Code for CS50

The text editor that is utilized for this course is **Visual Studio Code**, aka VS Code, affectionately referred to as **cs50.dev**, which can be accessed via that same URL.

One of the most important reasons I utilize VS Code is that it has all the software required for the course already pre-loaded on it. This course and the instructions herein were designed with VS Code in mind.

I learned that manually installing the necessary software for the course on my own computer is a cumbersome headache. Best always to utilize VS Code for assignments in this course.

I found I can open VS Code at [cs50.dev](https://cs50.dev).

The IDE can be divided into a number of regions:

![IDE](https://cs50.harvard.edu/x/2024/notes/1/vscode.png)

Notice that there is a **file explorer** on the left side where I can find my files. Further, notice that there is a region in the middle called a **text editor** where I can edit my program. Finally, there is a **command line interface**, known as a **CLI**, **command line**, or **terminal window**, where I can send commands to the computer in the cloud.

I also noticed in the **graphical user interface** (GUI) on the left-hand bar, various tools and a file explorer.

Because this IDE is pre-configured with all the necessary software, I agreed to use it to complete all assignments for this course.

## Hello World

I used three commands to write, compile, and run my first program:

`code hello.c`

`make hello`

`./hello`

The first command, `code hello.c` creates a file and allows me to type instructions for this program. The second command, `make hello`, compiles the file from my instructions in C and creates an executable file called `hello`. The last command, `./hello`, runs the program called `hello`.

I built my first program in C by typing `code hello.c` into the terminal window. I deliberately lowercased the entire filename and included the `.c` extension. Then, in the text editor that appears, I wrote code as follows:

```c
// A program that says hello to the world

#include <stdio.h>

int main(void)
{
    printf("hello, world\n");
}
```

I noted that every single character above serves a purpose. If I type it incorrectly, the program will not run. `printf` is a function that can output a line of text. I noticed the placement of the quotes and the semicolon. Further, I noticed that the `\n` creates a new line after the words `hello, world`.

Clicking back in the terminal window, I compiled my code by executing `make hello`. I noticed that I am omitting `.c`. `make` is a build tool that will compile my `hello.c` file and turn it into a program called `hello`. If executing this command results in no errors, I can proceed. If not, I double-checked my code to ensure it matches the above.

Now, I typed `./hello` and my program executed saying `hello, world`.

Now, I opened the file explorer on the left. I noticed that there is now both a file called `hello.c` and another file called `hello`. `hello.c` contains my source code that can be read by humans and the compiler. `hello` is an executable file containing machine code that the computer can run directly.

## From Scratch to C

In Scratch, I utilized the `say` block to display any text on the screen. Indeed, in C, I learned I have a function called `printf` that does exactly this.

I noticed my code already invokes this function:

`printf("hello, world\n");`

I noticed that the `printf` function is called. The argument passed to `printf` is `hello, world\n` surrounded by double quotes. The statement of code is closed with a `;`.

I learned that errors in code are common, especially in regards to syntax like semicolons and quotes. I modified my code as follows:

```c
// \n is missing

#include <stdio.h>

int main(void)
{
    printf("hello, world");
}
```

I noticed the `\n` is now gone.

In my terminal window, I ran `make hello`. Because I changed my program, I have to re-compile my program.

Typing `./hello` in the terminal window, I observed how my program changed. This `\` character is called an **escape character** that tells the compiler that `\n` is a special instruction to create a line break.

I learned there are other escape characters I can use:

`\n`  create a new line
`\r`  return to the start of a line
`\"`  print a double quote
`\'`  print a single quote
`\\`  print a backslash

I restored my program to the following:

```c
// A program that says hello to the world

#include <stdio.h>

int main(void)
{
    printf("hello, world\n");
}
```

I noticed the semicolon and `\n` have been restored.

## Header Files and CS50 Manual Pages

The statement at the start of the code `#include <stdio.h>` is a very special command that tells the compiler that I want to use the capabilities of a library called `stdio.h`, a **header file**. This allows me, among many other things, to utilize the `printf` function. I noticed, it’s not called studio: it’s `stdio.h`.

A **library** is a collection of code created by someone. Libraries are collections of pre-written code and functions that others have written in the past that I can utilize in my code.

I found I can read about all the capabilities of this library on the **Manual Pages**. The Manual Pages provide a means by which to better understand what various commands do and how they function.

It turns out that CS50 has its own library called `cs50.h`. There are numerous functions that are included that provide training wheels while I get started in C:

`get_char`
`get_double`
`get_float`
`get_int`
`get_long`
`get_string`

These libraries have been pre-installed for me at `cs50.dev`. If I were attempting to use these libraries on my own computer, I would likely have to install them. This is why I should use `cs50.dev` in this course, as it has all necessary software installed for me.

I decided to use this library in my program.

## Hello, You

I recalled that in Scratch I had the ability to ask the user, “What’s your name?” and say “hello” with that name appended to it.

In C, I found I can do the same. I modified my code as follows:

```c
// get_string and printf with incorrect placeholder

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string answer = get_string("What's your name? ");
    printf("hello, answer\n");
}
```

The `get_string` function is used to get a string from the user. Then, the variable `answer` is passed to the `printf` function.

Running `make hello` again in the terminal window, I noticed that numerous errors appear.

Looking at the errors, `string` and `get_string` are not recognized by the compiler. I realized I need to provide the compiler with these definitions by adding a library called `cs50.h`. Also, I noticed that `answer` is not provided as I intended. I modified my code as follows:

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

The `get_string` function is used to get a string from the user. Then, the variable `answer` is passed to the `printf` function. `%s` tells the `printf` function to prepare itself to receive a string.

Now, running `make hello` again in the terminal window, I could run my program by typing `./hello`. The program now asks for my name and then says hello with my name attached, as intended.

`answer` is a special holding place I call a **variable**. `answer` is of type `string` and can hold any string within it. There are many data types, such as `int`, `bool`, `char`, and many others.

`%s` is a placeholder called a **format code** that tells the `printf` function to prepare to receive a string. `answer` is the string being passed to `%s`.

## Linux

I have been using the CLI to make and run my program.

I found the CLI is often more useful than the GUI for executing commands and working with my files.

In the terminal window, the CLI, some common commands I may use include:

* `cd`, for changing my current directory (folder)
* `cp`, for copying files and directories
* `ls`, for listing files in a directory
* `mkdir`, for making a directory
* `mv`, for moving (renaming) files and directories
* `rm`, for removing (deleting) files
* `rmdir`, for removing (deleting) directories

The most commonly used is `ls` which will list all the files in the current directory. I went ahead and typed `ls` into the terminal window and hit enter. I saw all the files in the current folder.

## Conditionals

Another building block I utilized within Scratch was conditionals. For example, I might want to do one thing if x is greater than y. Further, I might want to do something else if that condition is not met.

I looked at a few examples from Scratch.

In C, I learned I can compare two values as follows:

```c
// Conditionals that are mutually exclusive

if (x < y)
{
    printf("x is less than y\n");
}
else
{
    printf("x is not less than y\n");
}
```

I noticed how if x < y, one outcome occurs. If x is not less than y, then another outcome occurs.

Similarly, I planned for three possible outcomes:

```c
// Conditional that isn't necessary

if (x < y)
{
    printf("x is less than y\n");
}
else if (x > y)
{
    printf("x is greater than y\n");
}
else if (x == y)
{
    printf("x is equal to y\n");
}
```

I noticed that not all these lines of code are required. I asked myself, "How could I eliminate the unnecessary calculation above?"

I guessed that I can improve this code as follows:

```c
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
```

I noticed how the final statement is replaced with `else`.

## Types

I learned there are many data types that are available within C:

* `bool`
* `char`
* `float`
* `int`
* `long`
* `string`
* ...

## Format Codes

Earlier, I recalled that I used a placeholder `%s` for a string in `printf`. This placeholder is called a **format code**.

`printf` allows for many format codes. Here is a non-comprehensive list of ones I may utilize in this course:

* `%c`
* `%f`
* `%i`
* `%li`
* `%s`

`%c` is used for `char` (character) variables. `%f` is used for `float` (floating-point) variables. `%i` is used for `int` or integer variables. `%li` is used for `long` integer variables. `%s` is used for `string` variables. I can find out more about this on the Manual Pages.

I will be using many of C’s available data types throughout this course.

## Variables

In C, I learned I can assign a value to an `int` or integer as follows:

```c
int counter = 0;
```

I noticed how a variable called `counter` of type `int` is assigned the value 0.

C can also be programmed to add one to `counter` as follows:

```c
counter = counter + 1;
```

I noticed how 1 is added to the value of `counter`.

This can be also represented as:

```c
counter += 1;
```

This can be further simplified to:

```c
counter++;
```

I noticed how the `++` is used to add 1.

I can also subtract one from `counter` as follows:

```c
counter--;
```

I noticed how, in this syntax, 1 is removed from the value of `counter`.

## compare.c

Using this new knowledge about how to assign values to variables, I programmed my first conditional statement.

In the terminal window, I typed `code compare.c` and wrote code as follows:

```c
// Conditional, Boolean expression, relational operator

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
}
```

I noticed that I create two variables, an `int` or integer called `x` and another called `y`. The values of these are populated using the `get_int` function.

I can run my code by executing `make compare` in the terminal window, followed by `./compare`. If I get any error messages, I should check my code for errors.

I improved my program by coding as follows:

```c
// Conditionals

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

I noticed that all potential outcomes are now accounted for.

I can re-make and re-run my program and test it out.

Examining these programs in various flow charts, I can see the efficiency of our code design decisions. Nearly any block of code can be translated to visual form.

## agree.c

Considering another data type called a `char`, I started a new program by typing `code agree.c` into the terminal window.

Where a `string` is a series of characters, a `char` is a single character.

In the text editor, I wrote code as follows:

```c
// Comparing against lowercase char

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user to agree
    char c = get_char("Do you agree? ");

    // Check whether agreed
    if (c == 'y')
    {
        printf("Agreed.\n");
    }
    else if (c == 'n')
    {
        printf("Not agreed.\n");
    }
}
```

I noticed that single quotes are utilized for single characters (`char` type), while double quotes are used for strings. Further, I noticed that `==` ensures that something is equal to something else, where a single equal sign would have a very different function in C.

I can test my code by typing `make agree` into the terminal window, followed by `./agree`.

I can also allow for the inputting of uppercase and lowercase characters:

```c
// Comparing against lowercase and uppercase char

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user to agree
    char c = get_char("Do you agree? ");

    // Check whether agreed
    if (c == 'y')
    {
        printf("Agreed.\n");
    }
    else if (c == 'Y')
    {
        printf("Agreed.\n");
    }
    else
    {
        printf("Not agreed.\n");
    }
}
```

I noticed that additional options are offered. However, this is not efficient code.

I can improve this code as follows:

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

I noticed that `||` effectively means **or**.

## Loops and meow.c

I can also utilize the loop building block from Scratch in my C programs.

In my terminal window, I typed `code meow.c` and wrote code as follows:

```c
// Opportunity for better design

#include <stdio.h>

int main(void)
{
    printf("meow\n");
    printf("meow\n");
    printf("meow\n");
}
```

I noticed this does as intended but has an opportunity for better design. Code is repeated over and over.

I improved my program by modifying my code as follows:

```c
// Better design

#include <stdio.h>

int main(void)
{
    int i = 3;
    while (i > 0)
    {
        printf("meow\n");
        i--;
    }
}
```

I noticed that I create an `int` called `i` and assign it the value 3. Then, I create a **while loop** that will run as long as `i > 0`. Then, the loop runs. Every time 1 is subtracted from `i` using the `i--` statement.

Similarly, I can implement a count-up of sorts by modifying my code as follows:

```c
// Print values of i

#include <stdio.h>

int main(void)
{
    int i = 1;
    while (i <= 3)
    {
        printf("meow\n");
        i++;
    }
}
```

I noticed how our counter `i` is started at 1. Each time the loop runs, it will increment the counter by 1. Once the counter is greater than 3, it will stop the loop.

Generally, in computer science, I count from zero. Best to revise my code as follows:

```c
// Better design

#include <stdio.h>

int main(void)
{
    int i = 0;
    while (i < 3)
    {
        printf("meow\n");
        i++;
    }
}
```

I noticed I now count from zero.

Another tool in my toolbox for looping is a **for loop**.

I can further improve the design of my `meow.c` program using a for loop. I modified my code as follows:

```c
// Better design

#include <stdio.h>

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        printf("meow\n");
    }
}
```

I noticed that the for loop includes three arguments. The first argument `int i = 0` starts our counter at zero. The second argument `i < 3` is the condition that is being checked. Finally, the argument `i++` tells the loop to increment by one each time the loop runs.

I can even loop forever using the following code:

```c
// Infinite loop

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    while (true)
    {
        printf("meow\n");
    }
}
```

I noticed that `true` will always be the case. Therefore, the code will always run. I will lose control of my terminal window by running this code. I can break from an infinite loop by hitting `control-C` on my keyboard (this sends a SIGINT signal to terminate the program).

I can ask the user how many times to meow by modifying the code as follows:

```c
// Prompts user for n.

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n = get_int("What's n? ");

    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}
```

I noticed that `n` is defined by the user. Then, there are `n` meows.

What happens if the user inputs something less than zero? I modified my code as follows:

```c
// Prompts user again if need be. (Poor design.)

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n = get_int("What's n? ");
    if (n < 0)
    {
        n = get_int("What's n? ");
    }

    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}
```

I noticed that this may stop the user from typing a number less than zero once. But what happens if they do it multiple times?

I improved my code as follows:

```c
// Uses a loop with continue/break.

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    while (true)
    {
        n = get_int("What's n? ");
        if (n < 0)
        {
            continue;
        }
        else
        {
            break;
        }
    }

    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}
```

I noticed that the while loop will run forever until `n` is greater than or equal to zero.

Still, this code could be improved further:

```c
// Uses a loop with just break.

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    while (true)
    {
        n = get_int("What's n? ");
        if (n >= 0)
        {
            break;
        }
    }

    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}
```

I noticed how my prior code is simplified, removing unnecessary lines of code.

Similar to a while loop, I could implement this code using a **do-while loop**:

```c
// Uses a do-while loop instead.

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("What's n? ");
    }
    while (n < 0);

    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}
```

I noticed that the `do` will always run at least once. That portion of code will loop while `n` is less than zero.

A critical eye may see that I could abstract away the portion of the code that meows.

## Functions

While I will provide much more guidance later, I learned I can create my own function within C as follows:

```c
void meow(void)
{
    printf("meow\n");
}
```

The initial `void` means that the function does not return any values. The `(void)` means that no values are being provided to the function.

This function can be used in the main function as follows:

```c
// Abstraction

#include <stdio.h>

void meow(void);

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        meow();
    }
}

// Meow once
void meow(void)
{
    printf("meow\n");
}
```

I noticed how the `meow` function is called with the `meow()` instruction. This is possible because the `meow` function is defined at the bottom of the code, and the **prototype** of the function is provided at the top of the code as `void meow(void)`.

My `meow` function can be further modified to accept input:

```c
// Abstraction with parameterization

#include <stdio.h>

void meow(int n);

int main(void)
{
    meow(3);
}

// Meow some number of times
void meow(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}
```

I noticed that the prototype has changed to `void meow(int n)` to show that `meow` accepts an `int` as its input.

When working with variables and functions, it’s important to understand the **scope** of a variable. I considered the following code:

```c
// Demonstrates scope

#include <stdio.h>

void meow(int n);

int main(void)
{
    int n = 3;
    meow(n);
}

// Meow some number of times
void meow(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}
```

I noticed how `n` is defined in the `main` function. Because of that, `n` is only in the scope of the `main` function. The only way that the `meow` function is able to use `n` is that a copy of `n` is passed to the `meow` function. `meow` is not using the original `n` from the `main` function. Instead, it is using its own copy of `n`.

With some modification to my code, I can get user input:

```c
// User input

#include <cs50.h>
#include <stdio.h>

void meow(int n);

int main(void)
{
    int n;
    do
    {
        n = get_int("Number: ");
    }
    while (n < 1);
    meow(n);
}

// Meow some number of times
void meow(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}
```

I noticed that `get_int` is used to obtain a number from the user. `n` is passed to `meow`.

I can even test to ensure that the input I get provided by the user is correct:

```c
// Return value

#include <cs50.h>
#include <stdio.h>

int get_positive_int(void);
void meow(int n);

int main(void)
{
    int n = get_positive_int();
    meow(n);
}

// Get number of meows
int get_positive_int(void)
{
    int n;
    do
    {
        n = get_int("Number: ");
    }
    while (n < 1);
    return n;
}

// Meow some number of times
void meow(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}
```

I noticed that a new function called `get_positive_int` asks the user for an integer while `n < 1`. After obtaining a positive integer, this function will return `n` back to the main function.

## Correctness, Design, Style

I learned code can be evaluated upon three axes.

First, **correctness** refers to “Does the code run as intended?” I can check the correctness of my code with `check50`.

Second, **design** refers to “How well is the code designed?” I can evaluate the design of my code using `design50`.

Finally, **style** refers to “How aesthetically pleasing and consistent is the code?” I can evaluate the style of my code with `style50`.

## Mario

Everything I’ve discussed today has focused on various building blocks of my work as an emerging computer scientist.

The following will help me orient toward working on a problem set for this class in general: How does one approach a computer science-related problem?

I imagined I wanted to emulate the visual of the game Super Mario Bros. Considering the four question blocks pictured, how could I create code that roughly represents these four horizontal blocks?

![Mario Question Marks](https://cs50.harvard.edu/x/2024/notes/1/mario.png)

In the terminal window, I typed `code mario.c` and code as follows:

```c
// Prints a row of 4 question marks

#include <stdio.h>

int main(void)
{
    printf("????\n");
}
```

I noticed that four question marks are printed.

Using a loop, I can more efficiently print the question marks:

```c
// Prints a row of 4 question marks with a loop

#include <stdio.h>

int main(void)
{
    for (int i = 0; i < 4; i++)
    {
        printf("?");
    }
    printf("\n");
}
```

I noticed how four question marks are printed here using a loop.

Similarly, I can apply this same logic to create three vertical blocks.

![Mario Blocks](https://cs50.harvard.edu/x/2024/notes/1/mario_blocks.png)

To accomplish this, I modified my code as follows:

```c
// Prints a column of 3 bricks with a loop

#include <stdio.h>

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        printf("#\n");
    }
}
```

I noticed how three vertical bricks are printed using a loop.

What if I wanted to combine these ideas to create a three-by-three group of blocks?

![Mario Grid](https://cs50.harvard.edu/x/2024/notes/1/mario_grid.png)

I can follow the logic above, combining the same ideas. I modified my code as follows:

```c
// Prints a 3-by-3 grid of bricks with nested loops

#include <stdio.h>

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
```

I noticed that one loop is inside another. The first loop defines what vertical row is being printed. For each row, three columns are printed. After each row, a new line is printed.

What if I wanted to ensure that the number of blocks is constant, that is, unchangeable? I modified my code as follows:

```c
// Prints a 3-by-3 grid of bricks with nested loops using a constant

#include <stdio.h>

int main(void)
{
    const int n = 3;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
```

I noticed how `n` is now a constant. It can never be changed.

As illustrated earlier in this lecture, I can abstract away functionality into functions. I considered the following code:

```c
// Helper function

#include <stdio.h>

void print_row(int width);
  
int main(void)
{
    const int n = 3;
    for (int i = 0; i < n; i++)
    {
        print_row(n);
    }
}

void print_row(int width)
{
    for (int i = 0; i < width; i++)
    {
        printf("#");
    }
    printf("\n");
}
```

I noticed how printing a row is accomplished through a new function.

## Operators

Operators refer to the mathematical operations that are supported by my compiler. In C, these mathematical operators include:

* `+` for addition
* `-` for subtraction
* `*` for multiplication
* `/` for division
* `%` for remainder

I will use all of these operators in this course.

I decided to implement my own calculator by typing `code calculator.c` in the terminal and modifying my code as follows:

```c
// Addition with int

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for x
    int x = get_int("What's x? ");

    // Prompt user for y
    int y = get_int("What's y? ");

    // Add numbers
    int z = x + y;

    // Perform addition
    printf("%i\n", z);
}
```

I noticed how I create a third variable `z` to store the sum of `x` and `y`, then print the result using `%i` (the format specifier for integers).

I could write more efficient code as follows:

```c
// Addition with int, without third variable

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for x
    int x = get_int("What's x? ");

    // Prompt user for y
    int y = get_int("What's y? ");

    // Perform addition
    printf("%i\n", x + y);
}
```

I noticed that I eliminated the need for the third variable `z` by performing the addition directly within the `printf` statement, making my code more concise.

I could use multiplication:

```c
// Doubles a number

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for x
    int x = get_int("What's x? ");

    // Double it
    printf("%i\n", x * 2);
}
```

I noticed how I use the multiplication operator `*` to double the input value, demonstrating another arithmetic operation beyond addition.

Integers in C can only count so high. I considered the following:

```c
// Overflow 

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int dollars = 1;
    while (true)
    {
        char c = get_char("Here's $%i. Double it and give to next person? ", dollars);
        if (c == 'y')
        {
            dollars *= 2;
        }
        else
        {
            break;
        }
    }
    printf("Here's $%i.\n", dollars);
}
```

I noticed how the program repeatedly doubles the dollar amount. Eventually, the integer will exceed its maximum value and “overflow,” wrapping around to a negative number or zero.

**Integer overflow** is when a calculation produces a value that exceeds the maximum storage capacity of the data type, causing the value to wrap around unpredictably.

One of C’s challenges is that while it provides me immense control over how memory is utilized, programmers have to be very aware of the potential pitfalls of memory management.

**Types** refer to the possible data that can be stored in a variable. For example, a `char` is designed to accommodate a single character like `a` or `2`.

Types are very important because each type has specific limits. For example, because of the limits in memory, the highest value of a signed `int` is typically 2147483647, while an unsigned `int` can reach 4294967295. If I attempt to count an `int` higher than its maximum, an integer overflow will result where an incorrect value will be stored in this variable.

The number of bits determines the range of values I can represent.

This can have catastrophic, real-world impacts.

I can solve this issue by using a `long` variable type:

```c
// long

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long dollars = 1;
    while (true)
    {
        char c = get_char("Here's $%li. Double it and give to next person? ", dollars);
        if (c == 'y')
        {
            dollars *= 2;
        }
        else
        {
            break;
        }
    }
    printf("Here's $%li.\n", dollars);
}
```

I noticed that I changed from `int` to `long` and use `%li` instead of `%i` in my format strings. A `long` can store much larger values than an `int`, delaying (but not eliminating) the overflow problem.

I may know that integers and floating point variables have a significant difference: The ability to represent numbers less than 1. I considered the following:

```c
// Division with ints, demonstrating truncation

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for x
    int x = get_int("What's x? ");

    // Prompt user for y
    int y = get_int("What's y? ");

    // Divide x by y
    printf("%i\n", x / y);
}
```

I noticed that when dividing two integers, C performs integer division and truncates (discards) any decimal portion. For example, `7 / 2` would give `3`, not `3.5`.

**Floating point imprecision** illustrates that there are limits to how precise computers can calculate numbers.

As I am coding, I should pay special attention to the types of variables I am using to avoid problems within my code.

I examined some examples of disasters that can occur through type-related errors.

Similarly, I can cast an integer to be a float. I considered the following:

```c
// Casting

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for x
    int x = get_int("What's x? ");

    // Prompt user for y
    int y = get_int("What's y? ");

    // Divide x by y
    printf("%f\n", (float) x / y);
}
```

I noticed how I cast `x` to a `float` before division using `(float) x`. This converts the integer to a floating-point number, allowing the division to produce a decimal result instead of truncating.

I could use floats throughout:

```c
// Floats

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for x
    float x = get_float("What's x? ");

    // Prompt user for y
    float y = get_float("What's y? ");

    // Divide x by y
    printf("%.50f\n", x / y);
}
```

I noticed that I use `get_float` for input and `%.50f` to display up to 50 decimal places, revealing the limitations of floating-point precision as the result may show unexpected digits due to binary representation constraints.

## Summing Up

In this lesson, I learned how to apply the building blocks I learned in Scratch to the C programming language. I learned…

* How to create my first program in C.
* How to use the command line.
* About predefined functions that come natively with C.
* How to use variables, conditionals, and loops.
* How to create my own functions to simplify and improve my code.
* How to evaluate my code on three axes: correctness, design, and style.
* How to integrate comments into my code.
* How to utilize types and operators and the implications of my choices.

This was CS50 Week 1 C.
