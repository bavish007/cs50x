# Lecture 2

## Table of Contents

* [Welcome!](#welcome)
* [Reading Levels](#reading-levels)
* [Debugging](#debugging)
* [Compiling](#compiling)
* [Arrays](#arrays)
* [Strings](#strings)
* [String Length](#string-length)
* [Command-Line Arguments](#command-line-arguments)
* [Exit Status](#exit-status)
* [Summing Up](#summing-up)

## Welcome

In my previous session, I learned about C, a text-based programming language.

This week, I learned I am going to take a deeper look at additional building blocks that will support my goals of learning more about programming from the bottom up.

Fundamentally, in addition to the essentials of programming, this course is about problem-solving. Accordingly, I will also focus further on how to approach computer science problems.

By the end of the course, I will learn how to use these aforementioned building blocks to solve a whole host of computer science problems.

I took for granted many of these solutions provided by computer science.

## Reading Levels

One of the real-world problems I will solve in this course is understanding reading levels.

With the help of some of my peers, I explored readings at various reading levels.

I will be quantifying reading levels this week as one of my many programming challenges.

## Debugging

I learned that everyone will make mistakes while coding.

**Debugging** is the process of locating and removing bugs from my code.

One of the debugging techniques I will use during this course to debug my code is called **rubber duck debugging**, where I can talk to an inanimate object (or myself) to help think through my code and why it is not working as intended. When I am having challenges with my code, I should consider speaking out loud to, quite literally, a rubber duck about the code problem. If I’d rather not talk to a small plastic duck, I am welcome to speak to a human near me!

I learned that the course has created the CS50 Duck and CS50.ai as tools that can help me debug my code.

I considered the following code:

```c
// Missing #include for stdio.h

int main(void)
{
    printf("hello, world\n");
}
```

I noticed how the `#include` directive for `stdio.h` is missing. This header file is required for the `printf` function to work properly. Without it, the compiler will not recognize the `printf` function and will generate an error.

Similarly, I considered the following code:

```c
// Misspelled stdio.h

#include <studio.h>

int main(void)
{
    printf("hello, world\n");
}
```

I noticed how `stdio.h` is misspelled as `studio.h`. This typo will cause a compilation error because the compiler cannot find a file called `studio.h`. The correct header file name is `stdio.h`, which stands for “standard input/output.”

I might forget to declare the type of a variable:

```c
// Missing cs50.h, variable's type, semicolon, %s, and second printf argument.

#include <stdio.h>

int main(void)
{
    name = get_string("What's your name? ")
    printf("hello, world\n");
}
```

I noticed there are multiple errors. First, the type of `name` is not declared. Second, the `cs50.h` library is missing to allow me to use `string`. Third, there’s a missing semicolon after the `get_string` call. Fourth, the `printf` statement doesn’t actually use the `name` variable.

I learned that some bugs will prompt an error message. Others are logical errors that will not prompt a message, but will result in unexpected behavior in my program.

The `printf` statement can be used to debug my code. I considered the following:

I considered the following image from last week:

![Mario](https://cs50.harvard.edu/x/2024/notes/2/mario.png)

I considered the following code that has a bug purposely inserted within it:

```c
// Buggy example for printf

#include <stdio.h>

int main(void)
{
    for (int i = 0; i <= 3; i++)
    {
        printf("#\n");
    }
}
```

I noticed that this code prints four blocks instead of three.

I typed `code buggy.c` into the terminal window and wrote the above code.

Running this code, four bricks appeared instead of the intended three.

I found `printf` is a very useful way of debugging my code. I could modify my code as follows:

```c
// Buggy example for printf

#include <stdio.h>

int main(void)
{
    for (int i = 0; i <= 3; i++)
    {
        printf("i is %i\n", i);
        printf("#\n");
    }
}
```

I noticed how this code outputs the value of `i` during each iteration of the loop such that I can debug my code.

Running this code, I saw numerous statements, including `i is 0`, `i is 1`, `i is 2`, and `i is 3`. Seeing this, I realized that further code needs to be corrected as follows:

```c
#include <stdio.h>

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        printf("#\n");
    }
}
```

I noticed the `<=` has been replaced with `<`.

This code can be further improved as follows:

```c
// Buggy example for debug50

#include <cs50.h>
#include <stdio.h>

void print_column(int height);

int main(void)
{
    int h = get_int("Height: ");
    print_column(h);
}

void print_column(int height)
{
    for (int i = 0; i <= height; i++)
    {
        printf("#\n");
    }
}
```

I noticed that compiling and running this code still results in a bug.

To address this bug, I used a new tool.

A second tool in debugging is called a **debugger**, a software tool created by programmers to help track down bugs in code.

In VS Code, a pre-configured debugger has been provided to me called `debug50`.

To utilize this debugger, first I set a **breakpoint** by clicking to the left of a line of my code, just to the left of the line number. When I clicked there, I saw a red dot appearing. I imagined this as a stop sign, asking the debugger to pause so that I can consider what’s happening in this part of my code.

![Breakpoint](https://cs50.harvard.edu/x/2024/notes/2/breakpoint.png)

Second, I ran `debug50 ./buggy`. I noticed that after the debugger comes to life and a line of my code will illuminate in a gold-like color. Quite literally, the code has paused at this line of code. I noticed in the top left corner how all local variables are being displayed, including `h`, which currently does not have a value. At the top of my window, I can click the **step over** button, and it will keep moving through my code. I noticed how the value of `i` increases as I step through the loop.

While this tool will not show me where my bug is, it will help me slow down and see how my code is running step by step. I can use **step into** as a way to look further into the details of my buggy code.

A third way of debugging is by speaking to a rubber duck, inanimate object, or a person to describe the problem I am facing and the specific steps I am taking to solve that problem as a means by which to discover my error.

Finally, also known as the *CS50 Duck*, can help me with debugging my code.

## Compiling

I recalled that last week, I learned about a compiler, a specialized computer program that converts source code into machine code that can be understood by a computer.

I convert source code into machine code using a very special piece of software called a **compiler**. Today, I was introduced to a compiler that will allow me to convert source code in the programming language C into machine code.

![Source Code](https://cs50.harvard.edu/x/2024/notes/2/source_code.png)

![Compiler](https://cs50.harvard.edu/x/2024/notes/2/compiler.png)

![Machine Code](https://cs50.harvard.edu/x/2024/notes/2/machine_code.png)

For example, I might have a computer program that looks like this:

```c
#include <stdio.h>

int main(void)
{
    printf("hello, world\n");
}
```

A compiler will take the above code and turn it into the machine code that might look something like this:

```
01010100 01001000 01001001 01010011
00100000 01001001 01010011 00100000
01000011 01010011 00110101 00110000
```

I noted that the above is only illustrative. The machine code for the problem above would be much longer.

VS Code, the programming environment provided to me as a CS50 student, utilizes a compiler called `clang` (which stands for “C Language Family Frontend”).

I can enter the following into the terminal window to compile my code: `clang -o hello hello.c`.

Command-line arguments are provided at the command line to `clang` as `-o hello hello.c`.

Running `./hello` in the terminal window, my program runs as intended.

I considered the following code from last week:

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string name = get_string("What's your name? ");
    printf("hello, %s\n", name);
}
```

To compile this code, I can type `clang -o hello hello.c -lcs50`.

If I were to type `make hello`, it runs a command that executes `clang` to create an output file that I can run as a user.

VS Code has been pre-programmed such that `make` will run numerous command line arguments along with `clang` for my convenience as a user.

While the above is offered as an illustration, such that I can understand more deeply the process and concept of compiling code, using `make` in CS50 is perfectly fine and the expectation!

I learned that compiling involves four major steps, including the following:

First, **preprocessing** is where the header files in my code, designated by a `#` (such as `#include <cs50.h>`) are effectively copied and pasted into my file. During this step, the code from `cs50.h` is copied into my program. Similarly, just as my code contains `#include <stdio.h>`, code contained within `stdio.h` somewhere on my computer is copied to my program. This step can be visualized as follows:

```c
  string get_string(string prompt);
  int printf(string format, ...);

  int main(void)
  {
      string name = get_string("What's your name? ");
      printf("hello, %s\n", name);
  }
```

Second, **compiling** is where my program is converted into assembly code. This step can be visualized as follows:

```
...
main:
    .cfi_startproc
# BB#0:
    pushq    %rbp
.Ltmp0:
    .cfi_def_cfa_offset 16
.Ltmp1:
    .cfi_offset %rbp, -16
    movq    %rsp, %rbp
.Ltmp2:
    .cfi_def_cfa_register %rbp
    subq    $16, %rsp
    xorl    %eax, %eax
    movl    %eax, %edi
    movabsq    $.L.str, %rsi
    movb    $0, %al
    callq    get_string
    movabsq    $.L.str.1, %rdi
    movq    %rax, -8(%rbp)
    movq    -8(%rbp), %rsi
    movb    $0, %al
    callq    printf
    ...
```

Third, **assembling** involves the assembler (a tool in the compiler toolchain) converting my assembly code into machine code. This step can be visualized as follows:

```
01111111010001010100110001000110
00000010000000010000000100000000
00000000000000000000000000000000
00000000000000000000000000000000
00000001000000000011111000000000
00000001000000000000000000000000
00000000000000000000000000000000
...
```

Finally, during the **linking** step, pre-compiled machine code from my included libraries is combined with my code. The final executable file is then outputted.

```
01111111010001010100110001000110
00000010000000010000000100000000
00000000000000000000000000000000
00000000000000000000000000000000
00000001000000000011111000000000
00000001000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
10100000000000100000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
01000000000000000000000000000000
00000000000000000100000000000000
00001010000000000000000100000000
01010101010010001000100111100101
01001000100000111110110000010000
00110001110000001000100111000111
01001000101111100000000000000000
00000000000000000000000000000000
00000000000000001011000000000000
11101000000000000000000000000000
00000000010010001011111100000000
00000000000000000000000000000000
00000000000000000000000001001000
...
```

## Arrays

In Week 0, I talked about data types such as `bool`, `int`, `char`, `string`, etc.

Each data type requires a certain amount of system resources (these are typical sizes in the CS50 environment):

* `bool` 1 byte
* `int` 4 bytes
* `long` 8 bytes
* `float` 4 bytes
* `double` 8 bytes
* `char` 1 byte
* `string` ? bytes

Inside of my computer, I have a finite amount of memory available.

![Memory](https://cs50.harvard.edu/x/2024/notes/2/memory.png)

Physically, on the memory of my computer, I can imagine how specific types of data are stored on my computer. I might imagine that a `char`, which only requires 1 byte of memory, may look as follows:

![1 byte](https://cs50.harvard.edu/x/2024/notes/2/1_byte.png)

Similarly, an `int`, which requires 4 bytes, might look as follows:

![4 bytes](https://cs50.harvard.edu/x/2024/notes/2/4_bytes.png)

I can create a program that explores these concepts. Inside my terminal, I typed `code scores.c` and wrote code as follows:

```c
// Averages three (hardcoded) numbers

#include <stdio.h>

int main(void)
{
    // Scores
    int score1 = 72;
    int score2 = 73;
    int score3 = 33;

    // Print average
    printf("Average: %f\n", (score1 + score2 + score3) / 3.0);
}
```

I noticed that the number on the right is a floating point value of `3.0`, so that the calculation is rendered as a floating point value in the end.

Running `make scores` compiles the program. Then running `./scores` executes it.

I can imagine how these variables are stored in memory:

![Scores in Memory](https://cs50.harvard.edu/x/2024/notes/2/scores_memory.png)

**Arrays** are a sequence of values that are stored back-to-back in memory.

`int scores[3]` is a way of telling the compiler to provide me three back-to-back places in memory of size `int` to store three scores. Considering my program, I could revise my code as follows:

```c
// Averages three (hardcoded) numbers using an array

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Scores
    int scores[3];
    scores[0] = 72;
    scores[1] = 73;
    scores[2] = 33;

    // Print average
    printf("Average: %f\n", (scores[0] + scores[1] + scores[2]) / 3.0);
}
```

I noticed that `scores[0]` examines the value at this location of memory by indexing into the array called `scores` at location 0 to see what value is stored there.

I saw how, while the above code works, there is still an opportunity for improving my code. I revised my code as follows:

```c
// Averages three numbers using an array and a loop

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get scores
    int scores[3];
    for (int i = 0; i < 3; i++)
    {
        scores[i] = get_int("Score: ");
    }

    // Print average
    printf("Average: %f\n", (scores[0] + scores[1] + scores[2]) / 3.0);
}
```

I noticed how I index into `scores` by using `scores[i]` where `i` is supplied by the for loop.

I can simplify or abstract away the calculation of the average. I modified my code as follows:

```c
// Averages three numbers using an array, a constant, and a helper function

#include <cs50.h>
#include <stdio.h>

// Constant
const int N = 3;

// Prototype
float average(int length, int array[]);

int main(void)
{
    // Get scores
    int scores[N];
    for (int i = 0; i < N; i++)
    {
        scores[i] = get_int("Score: ");
    }

    // Print average
    printf("Average: %f\n", average(N, scores));
}

float average(int length, int array[])
{
    // Calculate average
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum += array[i];
    }
    return sum / (float) length;
}
```

I noticed that a new function called `average` is declared. Further, I noticed that a `const` or constant value of `N` is declared. Most importantly, I noticed how the `average` function takes `int array[]`, which means that the function can receive an array as a parameter.

Not only can arrays be containers: They can be passed between functions.

## Strings

A **string** is simply an array of values of type `char`: an array of characters.

To explore `char` and `string`, I typed `code hi.c` in the terminal window and wrote code as follows:

```c
// Prints chars

#include <stdio.h>

int main(void)
{
    char c1 = 'H';
    char c2 = 'I';
    char c3 = '!';

    printf("%c%c%c\n", c1, c2, c3);
}
```

I noticed that this will output a string of characters.

Similarly, I made the following modification to my code:

```c
// Prints chars' ASCII codes

#include <stdio.h>

int main(void)
{
    char c1 = 'H';
    char c2 = 'I';
    char c3 = '!';

    printf("%i %i %i\n", c1, c2, c3);
}
```

I noticed that ASCII codes are printed by replacing `%c` with `%i`.

Considering the following image, I saw how a string is an array of characters that begins with the first character and ends with a special character called a **NUL character** (note: NUL with one L is the ‘\0’ character, different from NULL with two L’s):

![HI with Terminator](https://cs50.harvard.edu/x/2024/notes/2/hi_terminator.png)

Imagining this in decimal, my array would look like the following:

![HI with Decimal](https://cs50.harvard.edu/x/2024/notes/2/hi_decimal.png)

I can imagine the above as follows:

```c
// Prints string

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = "HI!";
    printf("%s\n", s);
}
```

I noticed that all characters are represented within a string.

To further understand how a string works, I revised my code as follows:

```c
// Treats string as array

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = "HI!";
    printf("%c%c%c\n", s[0], s[1], s[2]);
}
```

I noticed how the `printf` statement presents three values from my array called `s`.

As before, I can replace `%c` with `%i` as follows:

```c
// Prints string's ASCII codes, including NUL

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = "HI!";
    printf("%i %i %i %i\n", s[0], s[1], s[2], s[3]);
}
```

I noticed that this prints the string’s ASCII codes, including NUL.

I imagined I want to say both `HI!` and `BYE!`. I modified my code as follows:

```c
// Multiple strings

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = "HI!";
    string t = "BYE!";

    printf("%s\n", s);
    printf("%s\n", t);
}
```

I noticed that two strings are declared and used in this example.

I can visualize this as follows:

![HI and BYE](https://cs50.harvard.edu/x/2024/notes/2/hi_bye.png)

I can further improve this code. I modified my code as follows:

```c
// Array of strings

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string words[2];

    words[0] = "HI!";
    words[1] = "BYE!";

    printf("%s\n", words[0]);
    printf("%s\n", words[1]);
}
```

I noticed that both strings are stored within a single array of type `string`.

I can consolidate my two strings into an array of strings.

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string words[2];

    words[0] = "HI!";
    words[1] = "BYE!";

    printf("%c%c%c\n", words[0][0], words[0][1], words[0][2]);
    printf("%c%c%c%c\n", words[1][0], words[1][1], words[1][2], words[1][3]);
}
```

I noticed that an array of words is created. It is an array of strings. Each word is stored in `words`.

## String Length

A common problem within programming, and perhaps C more specifically, is to discover the length of a string. How could I implement this in code? I typed `code length.c` in the terminal window and code as follows:

```c
// Determines the length of a string

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt for user's name
    string name = get_string("Name: ");

    // Count number of characters up until '\0' (aka NUL)
    int n = 0;
    while (name[n] != '\0')
    {
        n++;
    }
    printf("%i\n", n);
}
```

I noticed that this code loops until the NUL character is found.

This code can be improved by abstracting away the counting into a function as follows:

```c
// Determines the length of a string using a function

#include <cs50.h>
#include <stdio.h>

int string_length(string s);

int main(void)
{
    // Prompt for user's name
    string name = get_string("Name: ");
    int length = string_length(name);
    printf("%i\n", length);
}

int string_length(string s)
{
    // Count number of characters up until '\0' (aka NUL)
    int n = 0;
    while (s[n] != '\0')
    {
        n++;
    }
    return n;
}
```

I noticed that a new function called `string_length` counts characters until NUL is located.

Since this is such a common problem within programming, other programmers have created code in the `string.h` library to find the length of a string. I can find the length of a string by modifying my code as follows:

```c
// Determines the length of a string using a function

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Prompt for user's name
    string name = get_string("Name: ");
    int length = strlen(name);
    printf("%i\n", length);
}
```

I noticed that this code uses the `string.h` library, declared at the top of the file. Further, it uses a function from that library called `strlen`, which calculates the length of the string passed to it.

My code can stand on the shoulders of programmers who came before and use libraries they created.

`ctype.h` is another library that is quite useful. I imagined I wanted to create a program that converted all lowercase characters to uppercase ones. In the terminal window, I typed `code uppercase.c` and wrote code as follows:

```c
// Uppercases a string

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Before: ");
    printf("After:  ");
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        if (s[i] >= 'a' && s[i] <= 'z')
        {
            printf("%c", s[i] - 32);
        }
        else
        {
            printf("%c", s[i]);
        }
    }
    printf("\n");
}
```

I noticed that this code iterates through each value in the string. The program looks at each character. If the character is lowercase, it subtracts 32 from the character’s ASCII value to convert it to uppercase.

Recalling my previous work from last week, I remembered this ASCII values chart:

![ASCII](https://cs50.harvard.edu/x/2024/notes/2/ascii.png)

When an ASCII lowercase letter (a-z) has 32 subtracted from it, it results in the uppercase version of that same letter. I noted this only works for ASCII letters a-z, not for accented or non-ASCII characters.

While the program does what I want, there is an easier way using the `ctype.h` library. I modified my program as follows:

```c
// Uppercases string using ctype library (and an unnecessary condition)

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Before: ");
    printf("After:  ");
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        if (islower(s[i]))
        {
            printf("%c", toupper(s[i]));
        }
        else
        {
            printf("%c", s[i]);
        }
    }
    printf("\n");
}
```

I noticed that the program iterates through each character of the string. The `toupper` function is passed `s[i]`. Each character (if lowercase) is converted to uppercase.

It’s worth mentioning that `toupper` automatically knows to uppercase only lowercase characters. Hence, my code can be simplified as follows:

```c
// Uppercases string using ctype library

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Before: ");
    printf("After:  ");
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        printf("%c", toupper(s[i]));
    }
    printf("\n");
}
```

I noticed that this code uppercases a string using the `ctype` library.

I found I can read about all the capabilities of the `ctype` library on the Manual Pages.

## Command-Line Arguments

**Command-line arguments** are those arguments that are passed to my program at the command line. For example, all those statements I typed after `clang` are considered command line arguments. I can use these arguments in my own programs!

In my terminal window, I typed `code greet.c` and wrote code as follows:

```c
// Uses get_string

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string answer = get_string("What's your name? ");
    printf("hello, %s\n", answer);
}
```

I noticed that this says hello to the user.

Still, would it not be nice to be able to take arguments before the program even runs? I modified my code as follows:

```c
// Prints a command-line argument

#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        printf("hello, %s\n", argv[1]);
    }
    else
    {
        printf("hello, world\n");
    }
}
```

I noticed that this program knows both `argc`, the number of command line arguments, and `argv`, which is an array of strings passed as arguments at the command line.

Therefore, using the syntax of this program, executing `./greet David` would result in the program saying `hello, David`.

I can print each of the command-line arguments with the following:

```c
// Prints command-line arguments

#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    for (int i = 0; i < argc; i++)
    {
        printf("%s\n", argv[i]);
    }
}
```

I noticed how this code prints out each command-line argument on its own line. The first argument (`argv[0]`) is always the name of the program itself, followed by any arguments I provide when running the program.

## Exit Status

When a program ends, a special **exit code** is provided to the computer.

When a program exits without error, a status code of 0 is provided to the computer. Often, when an error occurs that results in the program ending, a status of 1 is provided to the computer.

I could write a program as follows that illustrates this by typing `code status.c` and writing code as follows:

```c
// Returns explicit value from main

#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Missing command-line argument\n");
        return 1;
    }
    printf("hello, %s\n", argv[1]);
    return 0;
}
```

I noticed that if I fail to provide `./status David`, I will get an exit status of 1. However, if I do provide `./status David`, I will get an exit status of 0.

I can type `echo $?` in the terminal to see the exit status of the last run command.

I can imagine how I might use portions of the above program to check if a user provided the correct number of command-line arguments.

## Summing Up

In this lesson, I learned more details about compiling and how data is stored within a computer. Specifically, I learned…

* Generally, how a compiler works.
* How to debug my code using four methods.
* How to utilize arrays within my code.
* How arrays store data in back-to-back portions of memory.
* How strings are simply arrays of characters.
* How to interact with arrays in my code.
* How command-line arguments can be passed to my programs.

This was CS50 Week 2 Arrays.
