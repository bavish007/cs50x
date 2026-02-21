# Artificial Intelligence

- [Welcome!](#welcome)
- [Generative Artificial Intelligence](#generative-artificial-intelligence)
- [Prompt Engineering and Copilot](#prompt-engineering-and-copilot)
- [AI](#ai)
- [Decision Trees](#decision-trees)
- [Minimax](#minimax)
- [Machine Learning](#machine-learning)
- [Deep Learning](#deep-learning)
- [Large Language Models](#large-language-models)
- [Summing Up](#summing-up)

## Welcome

I learned that in computer science and programming circles, rubber ducking or rubber duck debugging is the act of speaking to an inanimate object to be able to talk through a challenging problem like a bug in one’s code.

I explored how CS50 created our own rubber duck debugger at CS50.ai, which uses artificial intelligence (AI) as a way by which to interact with students to help them with their own challenging problems.

By engaging with this tool, I began understanding the potential of what AI can offer the world.

## Generative Artificial Intelligence

I learned that numerous AI tools have created the potential for artificially generated images to enter the world.

I discovered that up until years past, most of these tools had numerous tells that might indicate to an observer that an image is AI-generated.

However, I noticed that tools are becoming exceedingly good at generating these images.

Indeed, I realized that as technology improves, it will soon be almost, if not entirely, impossible for such images to be detected with the naked eye.

I learned that Generative AI can be used to create photos, video, music, and text.

## Prompt Engineering and Copilot

I learned that prompt engineering is the way by which an individual can ask good questions of an AI.

I explored how we use a system prompt to teach the AI how to interact with users. I learned that we teach the AI how to work with students using such a prompt.

I discovered that user prompts are those provided by users to interact with the AI. With these prompts, I saw how students interact with the AI.

I can implement this in code as follows:

```python
# Adds to system prompt

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

I can run this code with python chat.py. I can download this code here

I learned that Generative AI can also be used to generate code! This kind of functionality can amplify my abilities as a growing and well-practiced programmer.

I explored Copilot is one such tool for generating code. In CS50, I learned that we do not allow the use of generative AI, outside the course’s own tools. I saw that CS50 provides clear guidance for students, in our academic honesty policy, on what is considered reasonable and unreasonable use of AI.

## AI

I learned that AI has been with us for many decades! Software has long adapted to users. I saw that algorithms look for patterns in junk mail, in handwriting recognition, in creating movie and video recommendations, and in playing games.

In games, for example, I learned that step-by-step instructions may allow a computerized adversary to play a game of Breakout.

## Decision Trees

I learned that decision trees are used by an algorithm to decide what decision to make.

For example, in Breakout, I explored how an algorithm may consider what choice to make based on the instructions in the code:

```
While game is ongoing:
  If ball is left of paddle:
    Move paddle left
  Else if ball is right of paddle:
    Move paddle right
  Else:
    Don't move paddle
```

I realized that with most games, they attempt to minimize the number of calculations required to compete with the player.

## Minimax

I learned that AI is often good at gameplay because it reduces moves and outcomes to mathematical values.

I can imagine where an algorithm may score outcomes as positive, negative, and neutral.

In tic-tac-toe, I saw that the AI may consider a board where the computer wins as 1 and one where the computer loses as -1.

I can imagine how a computer may look at a decision tree of potential outcomes and assign scores to each potential move.

I learned that the computer will attempt to win by maximizing its own score.

In the context of tic-tac-toe, I saw that the algorithm may conceptualize this as follows:

```
If player is X:
  For each possible move:
    Calculate score for board
  Choose move with highest score

Else if player is O:
    For each possible move:
        Calculate score for board
    Choose move with lowest score
```

This could be pictured as follows:

tictactoe with outcomes as 1 or -1 or 0

I learned that because computers are so powerful, they can crunch massive potential outcomes. However, I realized that the computers in our pockets or on our desks may not be able to calculate trillions of options for ever-more-complex game trees. I discovered that this is where machine learning can help.

## Machine Learning

I learned that machine learning is a way by which a computer can learn through reinforcement.

I saw that a computer can learn how to flip a pancake.

I also saw that a computer can learn how to play The Floor is Lava.

I learned that the computer repeats trial after trial after trial to discover what behaviors to repeat and those not to repeat.

Within much of AI-based algorithms, I explored concepts of explore vs. exploit, where the AI may randomly try something that may not be considered optimal. I learned that randomness can yield better outcomes. This can be represented in code as follows:

```
epsilon = 0.10

If random() < epsilon:
    Make a random move
Else:
    Make the move with the highest value
```

I noticed that epsilon represents the rate of randomness.

## Deep Learning

I learned that supervised learning is a form of AI-based learning where the human partners with the AI. For example, I might click the “spam” button in my email client to teach the AI what emails it should consider spam.

However, I realized that supervised learning does not scale well to larger problems. Hence, I learned about unsupervised learning is a means by which the AI can learn with minimal human intervention.

I discovered that deep learning uses neural networks whereby problems and solutions are explored.

For example, I learned that deep learning may attempt to predict whether a blue or red dot will appear somewhere on a graph. Consider the following image:

blue dots and red dots separated by a line

I learned that existing training data is used to predict an outcome. Further, I saw that more training data may be created by the AI to discover further patterns.

I learned that deep learning creates nodes (pictured below) that associate inputs and outputs.

Nodes connected to nodes

## Large Language Models

I learned that large language models (LLMs) are massive models that make predictions based on huge amounts of training.

I learned that just a few years ago, AI was not very good at completing and generating sentences. I saw that Google published a paper in 2017 regarding how these AIs can have their attention drawn to the relationships between various words.

I learned that Generative Pre-trained Transformer (GPT for short) are trained on the relationships between words.

I saw that the AI encodes words into embeddings to find relationships between words. Thus, through a huge amount of training, I learned that a massive neural network can predict the association between words - resulting in the ability for generative AI to generate content and even have conversations with users.

I also learned that sometimes, LLMs can hallucinate and provide incorrect information.

## Summing Up

In this lesson, I learned about some of the technology behind CS50.ai. Specifically, I discussed…

Generative Artificial Intelligence
Prompt Engineering
AI
Decision Trees
Minimax
Machine Learning
Deep Learning
Large Language Models

This was CS50!
