# Lecture 4

## Table of Contents

* [Welcome!](#welcome)
* [Pixel Art](#pixel-art)
* [Hexadecimal](#hexadecimal)
* [Memory](#memory)
* [Pointers](#pointers)
* [Strings](#strings)
* [Pointer Arithmetic](#pointer-arithmetic)
* [String Comparison](#string-comparison)
* [Copying and malloc](#copying-and-malloc)
* [Valgrind](#valgrind)
* [Garbage Values](#garbage-values)
* [Pointer Fun with Binky](#pointer-fun-with-binky)
* [Swapping](#swapping)
* [Overflow](#overflow)
* [scanf](#scanf)
* [File I/O](#file-io)
* [Summing Up](#summing-up)

## Welcome

Today, I learned we take off so many of the training wheels that I used to get my start in this class.

In previous weeks, I talked about images being made of smaller building blocks called pixels.

This week, I learned I will go into further detail about the zeros and ones that make up these images. In particular, I will be going deeper into the fundamental building blocks that make up files, including images.

Further, I will discuss how to access the underlying data stored in computer memory.

As I began today, I knew that the concepts covered in this lecture may take some time to fully click.

## Pixel Art

I learned that **pixels** are squares, individual dots, of color that are arranged on an up-down, left-right grid.

I can imagine an image as a map of bits, where zeros represent black and ones represent white.

![Smiley](https://cs50.harvard.edu/x/2024/notes/4/smiley.png)

## Hexadecimal

**RGB**, or red, green, blue, are numbers that represent the amount of each of these colors. In Adobe Photoshop, I can see these settings as follows:

![Photoshop](https://cs50.harvard.edu/x/2024/notes/4/photoshop.png)

I noticed how the amount of red, blue, and green changes the color selected.

I saw from the image above that color is not just represented by three values. At the bottom of the window, there is a special value made up of numbers and characters. `255` is represented as `FF`. I asked myself, "Why might this be?"

**Hexadecimal** is a system of counting that has 16 counting values. They are as follows:

```
  0 1 2 3 4 5 6 7 8 9 A B C D E F
```

I noticed that `F` represents 15.

Hexadecimal is also known as **base-16**.

When counting in hexadecimal, each column is a power of 16.

The number 0 is represented as `00`.
The number 1 is represented as `01`.
The number 9 is represented by `09`.
The number 10 is represented as `0A`.
The number 15 is represented as `0F`.
The number 16 is represented as `10`.
The number 255 is represented as `FF`, because 16 x 15 (or F) is 240. Add 15 more to make 255. This is the highest number I can count using a two-digit hexadecimal system.

I learned that hexadecimal is useful because it can be represented using fewer digits. Hexadecimal allows me to represent information more succinctly.

## Memory

In weeks past, I recalled my artist rendering of concurrent blocks of memory. Applying hexadecimal numbering to each of these blocks of memory, I visualized these as follows:

![Memory](https://cs50.harvard.edu/x/2024/notes/4/memory.png)

I imagined how there may be confusion regarding whether the `10` block above may represent a location in memory or the value 10. Accordingly, by convention, all hexadecimal numbers are often represented with the `0x` prefix as follows:

![Memory with 0x](https://cs50.harvard.edu/x/2024/notes/4/memory_hex.png)

In my terminal window, I typed `code addresses.c` and wrote my code as follows:

```c
// Prints an integer

#include <stdio.h>

int main(void)
{
    int n = 50;
    printf("%i\n", n);
}
```

I noticed how `n` is stored in memory with the value 50.

I visualized how this program stores this value as follows:

![Memory 50](https://cs50.harvard.edu/x/2024/notes/4/memory_50.png)

## Pointers

The C language has two powerful operators that relate to memory:

* `&` Provides the address of something stored in memory.
* `*` Instructs the compiler to go to a location in memory.

I can leverage this knowledge by modifying my code as follows:

```c
// Prints an integer's address

#include <stdio.h>

int main(void)
{
    int n = 50;
    printf("%p\n", &n);
}
```

I noticed the `%p`, which allows me to view the address of a location in memory. `&n` can be literally translated as “the address of n.” Executing this code will return an address of memory beginning with `0x`.

A **pointer** is a variable that stores the address of something. Most succinctly, a pointer is an address in my computer’s memory.

I considered the following code:

```c
int n = 50;
int *p = &n;
```

I noticed that `p` is a pointer that contains the address of an integer `n`.

I modified my code as follows:

```c
// Stores and prints an integer's address

#include <stdio.h>

int main(void)
{
    int n = 50;
    int *p = &n;
    printf("%p\n", p);
}
```

I noticed that this code has the same effect as my previous code. I have simply leveraged my new knowledge of the `&` and `*` operators.

To illustrate the use of the `*` operator, I considered the following:

```c
// Stores and prints an integer's address

#include <stdio.h>

int main(void)
{
    int n = 50;
    int *p = &n;
    printf("%p\n", p);
}
```

I noticed that the `printf` line prints the integer’s address. `int *p` creates a pointer whose job is to store the memory address of an integer.

I can visualize my code as follows:

![Pointer](https://cs50.harvard.edu/x/2024/notes/4/pointer.png)

I noticed that the pointer seems rather large. Indeed, a pointer is usually stored as an 8-byte value. `p` is storing the address of the `50`.

I can more accurately visualize a pointer as one address that points to another:

![Pointer Arrow](https://cs50.harvard.edu/x/2024/notes/4/pointer_arrow.png)

## Strings

Now that I have a mental model for pointers, I can peel back a level of simplification that was offered earlier in this course.

I modified my code as follows:

```c
// Prints a string

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = "HI!";
    printf("%s\n", s);
}
```

I noticed that a string `s` is printed.

I recalled that a string is simply an array of characters. For example, `string s = "HI!"` can be represented as follows:

![HI](https://cs50.harvard.edu/x/2024/notes/4/hi.png)

However, I asked, "What is `s` really? Where is the `s` stored in memory?" As I can imagine, `s` needs to be stored somewhere. I visualized the relationship of `s` to the string as follows:

![HI Pointer](https://cs50.harvard.edu/x/2024/notes/4/hi_pointer.png)

I noticed how a pointer called `s` tells the compiler where the first byte of the string exists in memory.

I modified my code as follows:

```c
// Prints a string's address as well the addresses of its chars

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = "HI!";
    printf("%p\n", s);
    printf("%p\n", &s[0]);
    printf("%p\n", &s[1]);
    printf("%p\n", &s[2]);
    printf("%p\n", &s[3]);
}
```

I noticed the above prints the memory locations of each character in the string `s`. The `&` symbol is used to show the address of each element of the string. When running this code, I noticed that elements 0, 1, 2, and 3 are next to one another in memory.

Likewise, I modified my code as follows:

```c
// Declares a string with CS50 Library

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = "HI!";
    printf("%s\n", s);
}
```

I noticed that this code creates a string using the `cs50.h` library.

Taking off the training wheels, I modified my code again:

```c
// Declares a string without CS50 Library

#include <stdio.h>

int main(void)
{
    char *s = "HI!";
    printf("%s\n", s);
}
```

I noticed that `cs50.h` is removed. A string is implemented as a `char *`. This code will present the string that starts at the location of `s`. This code effectively removes the training wheels of the string data type offered by `cs50.h`. This is raw C code, without the scaffolding of the `cs50` library.

I can imagine how a string, as a data type, is created.

Last week, I learned how to create my own data type as a struct.

The cs50 library includes a type definition as follows: `typedef char *string`

This type definition, when using the cs50 library, is a simplified representation that allows one to use a custom data type called `string`.

## Pointer Arithmetic

**Pointer arithmetic** is the ability to do math on locations of memory.

I can modify my code to print out each memory location in the string as follows:

```c
// Prints a string's chars

#include <stdio.h>

int main(void)
{
    char *s = "HI!";
    printf("%c\n", s[0]);
    printf("%c\n", s[1]);
    printf("%c\n", s[2]);
}
```

I noticed that I am printing each character at the location of `s`.

Further, I can modify my code as follows:

```c
// Prints a string's chars via pointer arithmetic

#include <stdio.h>

int main(void)
{
    char *s = "HI!";
    printf("%c\n", *s);
    printf("%c\n", *(s + 1));
    printf("%c\n", *(s + 2));
}
```

I noticed that the first character at the location of `s` is printed. Then, the character at the location `s + 1` is printed, and so on.

Likewise, I considered the following:

```c
// Prints substrings via pointer arithmetic

#include <stdio.h>

int main(void)
{
    char *s = "HI!";
    printf("%s\n", s);
    printf("%s\n", s + 1);
    printf("%s\n", s + 2);
}
```

I noticed that this code prints the values stored at various memory locations starting with `s`.

## String Comparison

A string of characters is simply an array of characters identified by the location of its first byte.

Earlier in the course, I considered the comparison of integers. I could represent this in code by typing `code compare.c` into the terminal window as follows:

```c
// Compares two integers

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get two integers
    int i = get_int("i: ");
    int j = get_int("j: ");

    // Compare integers
    if (i == j)
    {
        printf("Same\n");
    }
    else
    {
        printf("Different\n");
    }
}
```

I noticed that this code takes two integers from the user and compares them.

In the case of strings, however, I learned one cannot compare two strings using the `==` operator.

Utilizing the `==` operator in an attempt to compare strings will attempt to compare the memory locations of the strings instead of the characters therein. Accordingly, I learned to use `strcmp`.

To illustrate this, I modified my code as follows:

```c
// Compares two strings' addresses

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get two strings
    char *s = get_string("s: ");
    char *t = get_string("t: ");

    // Compare strings' addresses
    if (s == t)
    {
        printf("Same\n");
    }
    else
    {
        printf("Different\n");
    }
}
```

I noticed that typing in `HI!` for both strings still results in the output of `Different`.

I asked, "Why are these strings seemingly different?" I used the following logic to visualize why:

![Strings in Memory](https://cs50.harvard.edu/x/2024/notes/4/strings_memory.png)

Therefore, the code for `compare.c` above is actually attempting to see if the memory addresses are different, not the strings themselves.

Using `strcmp`, I can correct my code:

```c
// Compares two strings using strcmp

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Get two strings
    char *s = get_string("s: ");
    char *t = get_string("t: ");

    // Compare strings
    if (strcmp(s, t) == 0)
    {
        printf("Same\n");
    }
    else
    {
        printf("Different\n");
    }
}
```

I noticed that `strcmp` can return 0 if the strings are the same.

To further illustrate how these two strings are living in two locations, I modified my code as follows:

```c
// Prints two strings

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get two strings
    char *s = get_string("s: ");
    char *t = get_string("t: ");

    // Print strings
    printf("%s\n", s);
    printf("%s\n", t);
}
```

I noticed how I now have two separate strings stored, likely at two separate locations.

I can see the locations of these two stored strings with a small modification:

```c
// Prints two strings' addresses

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get two strings
    char *s = get_string("s: ");
    char *t = get_string("t: ");

    // Print strings' addresses
    printf("%p\n", s);
    printf("%p\n", t);
}
```

I noticed that the `%s` has been changed to `%p` in the print statement.

## Copying and malloc

A common need in programming is to copy one string to another.

In my terminal window, I typed `code copy.c` and wrote code as follows:

```c
// Capitalizes a string

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Get a string
    string s = get_string("s: ");

    // Copy string's address
    string t = s;

    // Capitalize first letter in string
    t[0] = toupper(t[0]);

    // Print string twice
    printf("s: %s\n", s);
    printf("t: %s\n", t);
}
```

I noticed that `string t = s` copies the address of `s` to `t`. This does not accomplish what I am desiring. The string is not copied – only the address is. Further, I noticed the inclusion of `ctype.h`.

I visualized the above code as follows:

![Copy](https://cs50.harvard.edu/x/2024/notes/4/copy.png)

I noticed that `s` and `t` are still pointing at the same blocks of memory. This is not an authentic copy of a string. Instead, these are two pointers pointing at the same string.

Before I address this challenge, it’s important to ensure that I don’t experience a **segmentation fault** through my code, where I attempt to copy string `s` to string `t`, where string `t` does not exist. I can employ the `strlen` function as follows to assist with that:

```c
// Capitalizes a string, checking length first

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Get a string
    string s = get_string("s: ");

    // Copy string's address
    string t = s;

    // Capitalize first letter in string
    if (strlen(t) > 0)
    {
        t[0] = toupper(t[0]);
    }

    // Print string twice
    printf("s: %s\n", s);
    printf("t: %s\n", t);
}
```

I noticed that `strlen` is used to make sure string `t` has content. If it does not, nothing will be copied.

To be able to make an authentic copy of the string, I learned I will need to introduce two new building blocks. First, `malloc` allows me, the programmer, to allocate a block of a specific size of memory. Second, `free` allows me to tell the compiler to free up that block of memory I previously allocated.

I can modify my code to create an authentic copy of my string as follows:

```c
// Capitalizes a copy of a string

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    // Get a string
    char *s = get_string("s: ");

    // Allocate memory for another string
    char *t = malloc(strlen(s) + 1);

    // Copy string into memory, including '\0'
    for (int i = 0; i <= strlen(s); i++)
    {
        t[i] = s[i];
    }

    // Capitalize copy
    t[0] = toupper(t[0]);

    // Print strings
    printf("s: %s\n", s);
    printf("t: %s\n", t);
}
```

I noticed that `malloc(strlen(s) + 1)` creates a block of memory that is the length of the string `s` plus one. This allows for the inclusion of the null `\0` character in my final copied string. Then, the for loop walks through the string `s` and assigns each value to that same location on the string `t`.

It turns out that my code is inefficient. I modified my code as follows:

```c
// Capitalizes a copy of a string, defining n in loop too

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    // Get a string
    char *s = get_string("s: ");

    // Allocate memory for another string
    char *t = malloc(strlen(s) + 1);

    // Copy string into memory, including '\0'
    for (int i = 0, n = strlen(s); i <= n; i++)
    {
        t[i] = s[i];
    }

    // Capitalize copy
    t[0] = toupper(t[0]);

    // Print strings
    printf("s: %s\n", s);
    printf("t: %s\n", t);
}
```

I noticed that `n = strlen(s)` is defined now in the left-hand side of the for loop. It’s best not to call unneeded functions in the middle condition of the for loop, as it will run over and over again. When moving `n = strlen(s)` to the left-hand side, the function `strlen` only runs once.

The C Language has a built-in function to copy strings called `strcpy`. It can be implemented as follows:

```c
// Capitalizes a copy of a string using strcpy

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    // Get a string
    char *s = get_string("s: ");

    // Allocate memory for another string
    char *t = malloc(strlen(s) + 1);

    // Copy string into memory
    strcpy(t, s);

    // Capitalize copy
    t[0] = toupper(t[0]);

    // Print strings
    printf("s: %s\n", s);
    printf("t: %s\n", t);
}
```

I noticed that `strcpy` does the same work that my for loop previously did.

Both `get_string` and `malloc` return `NULL`, a special value in memory, in the event that something goes wrong. I can write code that can check for this `NULL` condition as follows:

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

I noticed that if the string obtained is of length 0 or `malloc` fails, `NULL` is returned. Further, I noticed that `free` lets the computer know I am done with this block of memory I created via `malloc`.

## Valgrind

**Valgrind** is a tool that can check to see if there are memory-related issues with my programs wherein I utilized `malloc`. Specifically, it checks to see if I free all the memory I allocated.

I considered the following code for `memory.c`:

```c
// Demonstrates memory errors via valgrind

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *x = malloc(3 * sizeof(int));
    x[1] = 72;
    x[2] = 73;
    x[3] = 33;
}
```

I noticed that running this program does not cause any errors. While `malloc` is used to allocate enough memory for an array, the code fails to free that allocated memory.

If I type `make memory` followed by `valgrind ./memory`, I will get a report from valgrind that will report where memory has been lost as a result of my program. One error that valgrind reveals is that I attempted to assign the value of 33 at `x` of 3, where I only allocated an array of size 3 (`x[0]`, `x[1]`, and `x[2]`). Another error is that I never freed `x`.

I can modify my code to free the memory of `x` as follows:

```c
// Demonstrates memory errors via valgrind

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *x = malloc(3 * sizeof(int));
    x[0] = 72;
    x[1] = 73;
    x[2] = 33;
    free(x);
}
```

I noticed that running valgrind again now results in no memory leaks or errors

## Garbage Values

When I ask the compiler for a block of memory, there is no guarantee that this memory will be empty.

It’s very possible that the memory I allocated was previously utilized by the computer. Accordingly, I may see junk or **garbage values**. This is a result of me getting a block of memory but not initializing it. For example, I considered the following code for `garbage.c`:

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int scores[1024];
    for (int i = 0; i < 1024; i++)
    {
        printf("%i\n", scores[i]);
    }
}
```

I noticed that running this code will allocate 1024 locations in memory for my array, but the for loop will likely show that not all values therein are 0. It’s always best practice to be aware of the potential for garbage values when I do not initialize blocks of memory to some other value like zero or otherwise.

## Pointer Fun with Binky

I watched a video from Stanford University that helped me visualize and understand pointers.

## Swapping

In the real world, a common need in programming is to swap two values. Naturally, it’s hard to swap two variables without a temporary holding space. In practice, I can type `code swap.c` and write code as follows to see this in action:

```c
// Fails to swap two integers

#include <stdio.h>

void swap(int a, int b);

int main(void)
{
    int x = 1;
    int y = 2;

    printf("x is %i, y is %i\n", x, y);
    swap(x, y);
    printf("x is %i, y is %i\n", x, y);
}

void swap(int a, int b)
{
    int tmp = a;
    a = b;
    b = tmp;
}
```

I noticed that while this code runs, it does not work. The values, even after being sent to the swap function, do not swap. I asked myself, "Why?"

When I pass values to a function, I am only providing copies. The **scope** of `x` and `y` is limited to the `main` function as the code is presently written. That is, the values of `x` and `y` created in the curly `{}` braces of the `main` function only have the scope of the `main` function. In my code above, `x` and `y` are being **passed by value**.

I considered the following image:

![Global Variables](https://cs50.harvard.edu/x/2024/notes/4/globals.png)

I noticed that global variables, which I have not used in this course, live in one place in memory. Various functions are stored in the **stack** in another area of memory.

Now, I considered the following image:

![Stack](https://cs50.harvard.edu/x/2024/notes/4/stack.png)

I noticed that `main` and `swap` have two separate **frames** or areas of memory. Therefore, I cannot simply pass the values from one function to another to change them.

I modified my code as follows:

```c
// Swaps two integers using pointers

#include <stdio.h>

void swap(int *a, int *b);

int main(void)
{
    int x = 1;
    int y = 2;

    printf("x is %i, y is %i\n", x, y);
    swap(&x, &y);
    printf("x is %i, y is %i\n", x, y);
}

void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
```

I noticed that variables are not passed by value but **by reference**. That is, the addresses of `x` and `y` are provided to the function. Therefore, the `swap` function can know where to make changes to the actual `x` and `y` from the `main` function.

I can visualize this as follows:

![Swap Pointers](https://cs50.harvard.edu/x/2024/notes/4/swap_pointers.png)

## Overflow

A **heap overflow** is when I overflow the heap, touching areas of memory I am not supposed to.

A **stack overflow** is when too many functions are called, overflowing the amount of memory available.

Both of these are considered **buffer overflows**.

## scanf

In CS50, I have created functions like `get_int` to simplify the act of getting input from the user.

`scanf` is a built-in function that can get user input.

I can reimplement `get_int` rather easily using `scanf` as follows:

```c
// Gets an int from user using scanf

#include <stdio.h>

int main(void)
{
    int n;
    printf("n: ");
    scanf("%i", &n);
    printf("n: %i\n", n);
}
```

I noticed that the value of `n` is stored at the location of `n` in the line `scanf("%i", &n)`.

However, attempting to reimplement `get_string` is not easy. I considered the following:

```c
// Dangerously gets a string from user using scanf with array

#include <stdio.h>

int main(void)
{
    char s[4];
    printf("s: ");
    scanf("%s", s);
    printf("s: %s\n", s);
}
```

I noticed that no `&` is required because array names in C act as pointers. Still, this program will not function correctly every time it is run. Nowhere in this program do I allocate enough memory for my intended string. Indeed, I don’t know how long of a string may be inputted by the user! Further, I don’t know what garbage values may exist at the memory location.

Further, my code could be modified as follows. However, I have to pre-allocate a certain amount of memory for a string:

```c
// Using malloc

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char *s = malloc(4);
    if (s == NULL)
    {
        return 1;
    }
    printf("s: ");
    scanf("%s", s);
    printf("s: %s\n", s);
    free(s);
    return 0;
}
```

I noticed that if a string that is four bytes is provided I might get an error.

Simplifying my code as follows, I can further understand this essential problem of pre-allocation:

```c
#include <stdio.h>

int main(void)
{
    char s[4];
    printf("s: ");
    scanf("%s", s);
    printf("s: %s\n", s);
}
```

I noticed that if I pre-allocate an array of size 4, I can type `cat` and the program functions. However, a string larger than this could create an error.

Sometimes, the compiler or the system running it may allocate more memory than I indicate. Fundamentally, though, the above code is unsafe. I cannot trust that the user will input a string that fits into my pre-allocated memory.

## File I/O

I learned I can read from and manipulate files. While this topic will be discussed further in a future week, I considered the following code for `phonebook.c`:

```c
// Saves names and numbers to a CSV file

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Open CSV file
    FILE *file = fopen("phonebook.csv", "a");

    // Get name and number
    char *name = get_string("Name: ");
    char *number = get_string("Number: ");

    // Print to file
    fprintf(file, "%s,%s\n", name, number);

    // Close file
    fclose(file);
}
```

I noticed that this code uses pointers to access the file.

I can create a file called `phonebook.csv` in advance of running the above code. After running the above program and inputting a name and phone number, I will notice that this data persists in my CSV file.

If I want to ensure that `phonebook.csv` exists prior to running the program, I can modify my code as follows:

```c
// Saves names and numbers to a CSV file, checking for NULL

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Open CSV file
    FILE *file = fopen("phonebook.csv", "a");
    if (file == NULL)
    {
        return 1;
    }

    // Get name and number
    char *name = get_string("Name: ");
    char *number = get_string("Number: ");

    // Print to file
    fprintf(file, "%s,%s\n", name, number);

    // Close file
    fclose(file);
}
```

I noticed that this program protects against a `NULL` pointer by invoking `return 1`.

I can implement my own copy program by typing `code cp.c` and writing code as follows:

```c
// Copies a file

#include <stdio.h>

typedef unsigned char BYTE;

int main(int argc, char *argv[])
{
    FILE *src = fopen(argv[1], "rb");
    FILE *dst = fopen(argv[2], "wb");

    BYTE b;

    while (fread(&b, sizeof(b), 1, src) != 0)
    {
        fwrite(&b, sizeof(b), 1, dst);
    }

    fclose(dst);
    fclose(src);
}
```

I noticed that this file creates my own data type called a `BYTE`, which is equivalent to the size of a `uint8_t`. Then, the file reads a `BYTE` and writes it to a file.

**BMPs** are also assortments of data that I can examine and manipulate. This week, I will be doing just that in my problem sets!

## Summing Up

In this lesson, I learned about pointers that provide me with the ability to access and manipulate data at specific memory locations. Specifically, I delved into…

* Pixel art
* Hexadecimal
* Memory
* Pointers
* Strings
* Pointer Arithmetic
* String Comparison
* Copying
* malloc and Valgrind
* Garbage values
* Swapping
* Overflow
* scanf
* File I/O

This was CS50 Week 4 Memory
