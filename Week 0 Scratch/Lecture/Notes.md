# Lecture 0

## Table of Contents

* [Welcome!](#welcome)
* [Visual Studio Code and chat.py](#visual-studio-code-and-chatpy)
* [Computer Science and Problem Solving](#computer-science-and-problem-solving)
* [ASCII](#ascii)
* [Unicode](#unicode)
* [RGB](#rgb)
* [Algorithms](#algorithms)
* [Pseudocode](#pseudocode)
* [What’s Ahead](#whats-ahead)
* [Scratch](#scratch)
* [Hello World](#hello-world)
* [Hello, You](#hello-you)
* [Meow, Loops, and Abstraction](#meow-loops-and-abstraction)
* [Conditionals](#conditionals)
* [Oscartime](#oscartime)
* [Ivy’s Hardest Game](#ivys-hardest-game)
* [Summing Up](#summing-up)

## Welcome

I learned that Artificial intelligence (AI) is providing new advancements and excitement in computer science and the wide world!

I discovered that while AI provides huge advancements, sometimes eliminating the human bottlenecks that can slow down processes, being able to understand, create, and organize code allows me to be a driver, a pilot, and an empowered creator through programming.

Therefore, rather than thinking about AI as a way to remove the need to learn the fundamentals, I considered how knowing the fundamentals and being further empowered by AI will lead to whole new opportunities for me and those I serve.

## Visual Studio Code and chat.py

I explored VS Code, which is an IDE or integrated development environment, where I can create code.

To get a taste of what is to come, I saw that I could program my own chatbot called `chat.py`.

On a system already configured for using OpenAI’s libraries, I learned I could program as follows.

In the text editor, I could type in the following code:

```python
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    input="In one sentence, what is CS50?",
    model="gpt-5"
)

print(response.output_text)
```

I noticed how a library from OpenAI is imported to give me abilities from that library. A chat client is created. Then, a question, called input is passed to the chat client for an answer. The response is then printed.

I found that I could improve upon this code by allowing the user to ask a question. I modified my code as follows:

```python
from openai import OpenAI

client = OpenAI()

prompt = input("Prompt: ")

response = client.responses.create(
    input=prompt,
    model="gpt-5"
)

print(response.output_text)
```

I noticed that `prompt` is now created, allowing the user to ask a question.

I learned that this program can be improved even more by providing a `system_prompt` to provide some further context and instructions to the chatbot:

```python
from openai import OpenAI

client = OpenAI()

user_prompt = input("Prompt: ")
system_prompt = "Limit your answer to one sentence. Pretend you're a cat."

response = client.responses.create(
    input=user_prompt,
    instructions=system_prompt,
    model="gpt-5"
)

print(response.output_text)
```

I noticed how `system_prompt` is used to provide further context and instructions.

I realized that with programming, I have the ability in ten lines of text to build very powerful programs!

I learned that the course has created its own rubber duck, the CS50 Duck, to help me in my work in this course.

I kept in mind the Academic Honesty Policy, which prohibits the use of any AI tool besides the CS50 Duck.

## Computer Science and Problem Solving

Essentially, I learned that computer programming is about taking some input and creating some output - thus solving a problem. What happens in between the input and output, what I could call a black box, is the focus of this course.

![input](https://cs50.harvard.edu/x/2024/notes/0/input.png)

![output](https://cs50.harvard.edu/x/2024/notes/0/output.png)

For example, I experimented with the idea of taking attendance for a class. I could use a system called unary (also called base-1) to count one finger at a time.

I learned that computers today count using a system called binary (also called base-2). It’s from the term **bi**nary digi**t** that we get a familiar term called **bit**. A bit is a zero or one: on or off.

I discovered that computers only speak in terms of zeros and ones. Zeros represent off. Ones represent on. Computers are millions, and perhaps billions, of transistors that are being turned on and off.

I imagined using a light bulb; a single bulb can only count from zero to one.

However, I saw that if I were to have three light bulbs, there are more options open to me!

Inside my devices, such as my iPhone or computer, I learned there are millions of metaphorical light bulbs called transistors that enable the activities conducted on these devices that I may take for granted each day.

As a heuristic, I imagined that the following values represent each possible place in my binary digit:

```
4 2 1
```

Using three light bulbs, I saw that the following could represent zero:

```
4 2 1
0 0 0
```

Similarly, the following would represent one:

```
4 2 1
0 0 1
```

By this logic, I proposed that the following equals two:

```
4 2 1
0 1 0
```

Extending this logic further, the following represents three:

```
4 2 1
0 1 1
```

Four would appear as:

```
4 2 1
1 0 0
```

I realized I could, in fact, using only three light bulbs count as high as seven!

```
4 2 1
1 1 1
```

I learned that computers use base-2 to count. This can be pictured as follows:

```
2^2  2^1  2^0
4    2    1
```

Therefore, I could say that it would require three bits (the four’s place, the two’s place, and the one’s place) to represent a number as high as seven.

Similarly, to count a number as high as eight, values would be represented as follows:

```
8 4 2 1
1 0 0 0
```

I learned that computers generally use eight bits (also known as a byte) to represent a number. For example, `00000101` is the number 5 in binary. `11111111` represents the number 255. I can imagine zero as follows:

```
128 64 32 16 8 4 2 1
0   0  0  0  0 0 0 0
```

## ASCII

Just as numbers are binary patterns of ones and zeros, I learned that letters are represented using ones and zeros, too!

Since there is an overlap between the ones and zeros that represent numbers and letters, I discovered the **ASCII** standard was created to map specific letters to specific numbers.

For example, the letter `A` was decided to map to the number 65. `01000001` represents the number 65 in binary. I visualized this as follows:

```
128 64 32 16 8 4 2 1
0   1  0  0  0 0 0 1
```

If I received a text message, the binary under that message might represent the numbers 72, 73, and 33. Mapping these out to ASCII, my message would look as follows:

```
H   I   !
72  73  33
```

I thought, "Thank goodness for standards like ASCII that allow us to agree upon these values!"

I reviewed an expanded map of ASCII values:

![ASCII Map](https://cs50.harvard.edu/x/2024/notes/0/ascii.png)

I explored ASCII further to learn more about it.

I learned that if each character is stored in exactly one 8-bit byte, I can encode at most 256 distinct character codes. ASCII uses only 128 of those (0-127).

## Unicode

I observed that as time has rolled on, there are more and more ways to communicate via text.

Since there were not enough digits in binary to represent all the various characters that could be represented by humans, I learned that the **Unicode** standard expanded the number of bits that can be transmitted and understood by computers. Unicode includes not only special characters, but emoji as well.

I saw there are emoji that I probably use every day. The following looked familiar to me:

```
😀 😃 😄 😁 😆 😅 😂 🙂 🙃 😉 😊 😇 😍 😘 😗 😙 😚 😋 😛 😜 😝 🤑 🤓 😎 🤗 😏 😶 😐 😑 😒 🙄 😬 😕 ☹️ 😟 😮 😯 😲 😳 😦 😧 😨
```

While the pattern of zeros and ones is standardized within Unicode, I noted that each device manufacturer may display each emoji slightly differently than another manufacturer.

I learned that more and more features are being added to the Unicode standard to represent further characters and emoji.

I decided to explore more about Unicode and emoji.

## RGB

I learned that zeros and ones can be used to represent color.

Red, green, and blue (called **RGB**) are a combination of three numbers.

```
72 73 33
```

Taking my previously used 72, 73, and 33, which said `HI!` via text, I learned this would be interpreted by image readers as a light shade of yellow. The red value would be 72, the green value would be 73, and the blue would be 33.

![RGB](https://cs50.harvard.edu/x/2024/notes/0/rgb.png)

I learned that the three bytes required to represent various colors of red, blue, and green (or RGB) make up each pixel (or dot) of color in any digital image. Images are simply collections of RGB values.

I discovered that zeros and ones can be used to represent images, videos, and music!

Videos are sequences of many images that are stored together, just like a flipbook.

Music can be represented similarly using various combinations of bytes.

## Algorithms

I learned that problem-solving is central to computer science and computer programming. An **algorithm** is a step-by-step set of instructions to solve a problem.

I imagined the basic problem of trying to locate a single name in a phone book.

I asked myself, "How might I go about this?"

One approach could be to simply read from page one to the next to the next until reaching the last page.

Another approach could be to search two pages at a time.

A final and perhaps better approach could be to go to the middle of the phone book and ask, “Is the name I am looking for to the left or to the right?” Then, repeat this process, cutting the problem in half and half and half.

I learned that each of these approaches could be called algorithms. The speed of each of these algorithms can be pictured as follows in what is called **big-O notation**:

![Big O](https://cs50.harvard.edu/x/2024/notes/0/big_o.png)

I noticed that the first algorithm, highlighted in red, has a big-O of $n$ because if there are 100 names in the phone book, it could take up to 100 tries to find the correct name. The second algorithm, where two pages were searched at a time, has a big-O of $n/2$ because I searched twice as fast through the pages. The final algorithm has a big-O of $\log_2 n$, as doubling the problem would only result in one more step to solve the problem.

I learned that programmers translate text-based, human instructions into code to solve problems.

## Pseudocode

I learned that **pseudocode** is human-readable instructions that often describe the steps of an algorithm.

The ability to create pseudocode is central to my success in both this class and in computer programming.

For example, considering the third algorithm above, I could compose pseudocode as follows:

```
1  Pick up phone book
2  Open to middle of phone book
3  Look at page
4  If person is on page
5      Call person
6  Else if person is earlier in book
7      Open to middle of left half of book
8      Go back to line 3
9  Else if person is later in book
10     Open to middle of right half of book
11     Go back to line 3
12 Else
13     Quit
```

I discovered that pseudocoding is such an important skill for at least two reasons. First, when I pseudocode before I create formal code, it allows me to think through the logic of my problem in advance. Second, when I pseudocode, I can later provide this information to others that are seeking to understand my coding decisions and how my code works.

I noticed that the language within my pseudocode has some unique features. First, some of these lines begin with verbs like *pick up*, *open*, *look at*. I learned later I will call these **functions**.

Second, I noticed that some lines include statements like `if` or `else if`. These are called **conditionals**.

Third, I noticed how there are expressions that can be stated as true or false, such as “person is earlier in the book.” I learned we call these **boolean expressions**.

Finally, I noticed how there are statements like “go back to line 3.” I learned we call these **loops**.

These building blocks are the fundamentals of programming.

In the context of **Scratch**, which I discussed below, I used each of the above basic building blocks of programming.

## What’s Ahead

I learned that I will be learning this week about Scratch, a visual programming language.

Then, in future weeks, I will learn about **C**. That will look something like this:

```c
#include <stdio.h>

int main(void)
{
  printf("hello, world\n");
}
```

By learning C, I found I will be far more prepared for future learning in other programming languages like Python.

I noticed how programmers have used **abstraction** to build off the work of other programmers. Rather than programming in ones and zeroes, programming languages were created to abstract away from the incredibly challenging task of programming in binary to more and more easy-to-use programming languages. I realized I can stand on the shoulders of others!

## Scratch

I explored **Scratch**, a visual programming language developed by MIT.

I saw that Scratch utilizes the same essential coding building blocks that I covered earlier in this lecture.

I found Scratch to be a great way to get into computer programming because it allows me to play with these building blocks in a visual manner, not having to be concerned about the syntax of curly braces, semicolons, parentheses, and the like.

I saw the Scratch IDE (integrated development environment) looks like the following:

![Scratch IDE](https://cs50.harvard.edu/x/2024/notes/0/scratch.png)

I noticed that on the left, there is a palette of building blocks that I can use in my programming. To the immediate right of the building blocks, there is the area to which I can drag blocks to build a program. To the right of that, I saw the stage where a cat stands. The stage is where my programming comes to life.

I learned that Scratch operates on a coordinate system as follows:

![Coordinates](https://cs50.harvard.edu/x/2024/notes/0/coordinates.png)

I noticed that the center of the stage is at coordinate (0,0). Right now, the cat’s position is at that same position.

## Hello World

To begin, I dragged the “when green flag clicked” building block to the programming area. Then, I dragged the `say` building block to the programming area and attached it to the previous block.

![Hello World](https://cs50.harvard.edu/x/2024/notes/0/hello_world.png)

I noticed that when I click the green flag now on the stage, the cat says, “hello, world.”

I realized this illustrates quite well what I was discussing earlier regarding programming:

![Black Box](https://cs50.harvard.edu/x/2024/notes/0/black_box.png)

I noticed that the input `hello, world` is passed to the function `say`, and the side effect of that function running is the cat saying `hello, world`.

## Hello, You

I found I can make my program more interactive by having the cat say hello to someone specific. I modified my program as below:

![Hello You](https://cs50.harvard.edu/x/2024/notes/0/hello_you.png)

I noticed that when the green flag is clicked, the function `ask` is run. The program prompts me, the user, `What's your name?` It then stores that name in the variable called `answer`. The program then passes `answer` to a special function called `join`, which combines two strings of text `hello,` and whatever name was provided. The value of `answer` is passed as an argument to `join`. These collectively are passed to the `say` function. The cat says, `Hello,` and a name. My program is now interactive.

Throughout this course, I learned I will be providing inputs into an algorithm and getting outputs. This can be pictured in terms of the above program as follows:

![Algorithm](https://cs50.harvard.edu/x/2024/notes/0/algorithm.png)

I noticed that the inputs `hello,` and `answer` are provided to `join`, which returns `hello, David`. This return value is then passed to `say`, which produces the side effect of the cat speaking.

Quite similarly, I modified my program as follows:

![Speak](https://cs50.harvard.edu/x/2024/notes/0/speak.png)

I noticed that this program, when the green flag is clicked, passes the same variable, joined with `hello,`, to a function called `speak`.

## Meow, Loops, and Abstraction

Along with pseudocoding, I learned that **abstraction** is an essential skill and concept within computer programming.

Abstraction is the act of simplifying a problem into smaller and smaller problems.

For example, I imagined if I were hosting a huge dinner for my friends, the problem of having to cook the entire meal could be quite overwhelming! However, if I break down the task of cooking the meal into smaller and smaller tasks (or problems), the big task of creating this delicious meal might feel less challenging.

In programming, and even within Scratch, I can see abstraction in action. In my programming area, I programmed as follows:

![Meow](https://cs50.harvard.edu/x/2024/notes/0/meow.png)

I noticed that I am doing the same thing over and over again. Indeed, if I see myself repeatedly coding the same statements, I learned it’s likely the case that I could program more artfully – abstracting away this repetitive code.

I modified my code as follows:

![Repeat](https://cs50.harvard.edu/x/2024/notes/0/repeat.png)

I noticed that the loop does exactly as the previous program did. However, the problem is simplified by abstracting away the repetition to a block that repeats the code for me.

I learned I can even advance this further by using the `define` block, where I can create my own block (my own function)! I wrote code as follows:

![Define Meow](https://cs50.harvard.edu/x/2024/notes/0/define_meow.png)

I noticed that I am defining my own block called `meow`. The function plays the sound meow, and then waits one second. Below that, I can see that when the green flag is clicked, my `meow` function is repeated three times.

I saw I can even provide a way by which the function can take an input `n` and repeat a number of times:

![Meow n times](https://cs50.harvard.edu/x/2024/notes/0/meow_n_times.png)

I noticed how `n` is taken from “meow n times.” `n` is passed to the `meow` function through the define block.

Overall, I noticed how this process of refinement led to better and better-designed code. Further, I noticed how I created my own algorithm to solve a problem. I will be exercising both of these skills throughout this course.

## Conditionals

I learned that **conditionals** are an essential building block of programming, where the program looks to see if a specific condition has been met. If a condition is met, the program does something.

To illustrate a conditional, I wrote code as follows:

![If Touching](https://cs50.harvard.edu/x/2024/notes/0/if_touching.png)

I noticed that the `forever` block is utilized such that the `if` block is triggered over and over again, such that it can check continuously if the cat is touching the mouse pointer.

I modified my program as follows to integrate video sensing:

![Video Motion](https://cs50.harvard.edu/x/2024/notes/0/video_motion.png)

I remembered that programming is often a process of trial and error. If I get frustrated, I should take time to talk myself through the problem at hand. What is the specific problem that I am working on right now? What is working? What is not working?

## Oscartime

I learned that **Oscartime** is one of David’s own Scratch programs – though the music may haunt him because of the number of hours he listened to it while creating this program. I took a few moments to play through the Oscartime game myself.

![Oscartime](https://cs50.harvard.edu/x/2024/notes/0/oscartime.png)

Building Oscartime myself, I first added the lamp post.

![Lamp Post](https://cs50.harvard.edu/x/2024/notes/0/lamp_post.png)

Then, I wrote code as follows:

![Oscar Code](https://cs50.harvard.edu/x/2024/notes/0/oscar_code.png)

I noticed that moving my mouse over Oscar changes his costume. I learned more by exploring these code blocks.

Then, I modified my code as follows to create a falling piece of trash:

![Trash Code](https://cs50.harvard.edu/x/2024/notes/0/trash_code.png)

I noticed that the trash’s position on the y-axis always begins at 180. The x position is randomized. While the trash is above the floor, it goes down 1 pixel at a time. I learned more by exploring these code blocks.

Next, I modified my code as follows to allow for the possibility of dragging trash.

![Drag Trash](https://cs50.harvard.edu/x/2024/notes/0/drag_trash.png)

I learned more by exploring these code blocks.

Next, I implemented the scoring variables as follows:

![Scoring](https://cs50.harvard.edu/x/2024/notes/0/scoring.png)

I learned more by exploring these code blocks.

I went to try the full game Oscartime.

## Ivy’s Hardest Game

Moving away from Oscartime to **Ivy’s Hardest Game**, I could now imagine how to implement movement within my program.

My program has three main components.

First, I wrote code as follows:

![Movement](https://cs50.harvard.edu/x/2024/notes/0/movement.png)

I noticed that when the green flag is clicked, my sprite moves to the center of the stage at coordinates (0,0) and then listens for the keyboard and checks for walls forever.

Second, I added this second group of code blocks:

![Listen Keyboard](https://cs50.harvard.edu/x/2024/notes/0/listen_keyboard.png)

I noticed how I have created a custom `listen for keyboard` script. For each of my arrow keys on the keyboard, it will move the sprite around the screen.

Finally, I added this group of code blocks:

![Feel Walls](https://cs50.harvard.edu/x/2024/notes/0/feel_walls.png)

I noticed how I also have a custom `feel for walls` script. When a sprite touches a wall, it moves it back to a safe position – preventing it from walking off the screen.

I learned more by exploring these code blocks.

I learned that Scratch allows for many sprites to be on the screen at once.

Adding another sprite, I added the following code blocks to my program:

![Yale Sprite](https://cs50.harvard.edu/x/2024/notes/0/yale_sprite.png)

I noticed how the Yale sprite seems to get in the way of the Harvard sprite by moving back and forth. When it bumps into a wall, it turns around until it bumps the wall again. I learned more by exploring these code blocks.

I found I can even make a sprite follow another sprite. Adding another sprite, I added the following code blocks to my program:

![MIT Sprite](https://cs50.harvard.edu/x/2024/notes/0/mit_sprite.png)

I noticed how the MIT logo now seems to follow around the Harvard one. I learned more by exploring these code blocks.

I went to try the full game Ivy’s Hardest Game.

## Summing Up

In this lesson, I learned how this course sits in the wide world of computer science and programming. I learned…

* While AI can help remove human bottlenecks, learning the fundamentals in computer science and the foundational building blocks of programming will enable me to utilize emerging technologies better and better.
* Reasonable and unreasonable ways to utilize AI in this course.
* Problem-solving is the essence of the work of computer scientists.
* How numbers, text, images, music, and video are understood and represented by computers.
* The fundamental programming skill of pseudocoding.
* How abstraction will play a role in my future work in this course.
* The basic building blocks of programming including functions, conditionals, loops, and variables.
* How to build a project in Scratch.

This was CS50! Week 0 Scratch.
