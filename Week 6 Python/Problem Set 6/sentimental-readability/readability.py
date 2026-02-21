from cs50 import get_string # Imports function

# Get user input
text = get_string("Text: ")

# Initialize counters: Words (W), Letters (L), Sentences (S)
W = 0
L = 0
S = 0
a = len(text) # Text length
for i in range(a): # Count spaces
    if text[i] == " ":
        W += 1
W = W + 1 # Final word count

for i in range(a): # Count letters
    if text[i].isalpha() == True:
        L += 1

for i in range(a): # Count end punctuation
    if text[i] == "." or text[i] == "!" or text[i] == "?":
        S += 1

# Calculate Coleman-Liau index
index = round(0.0588 * (L / W * 100.0) - 0.296 * (S / W * 100.0) - 15.8)
if index < 1: # Grade < 1
    print("Before Grade 1\n")
elif index > 16: # Grade > 16
    print("Grade 16+\n")
else: # Print calculated grade
    print(f"Grade {index}")
