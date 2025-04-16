# generate_input.py
import os
import random

# Ensure the input folder exists
if not os.path.exists("input"):
    os.makedirs("input")

words = ["hello", "world", "mapreduce", "goodbye", "python", "code", "example", "input"]

with open("input/sample.txt", "w") as f:
    for i in range(1, 101):
        # Generate a sentence of 3 to 5 words chosen at random
        sentence = " ".join(random.choice(words) for _ in range(random.randint(3, 5)))
        f.write(sentence + "\n")

print("Generated input/sample.txt with 100 lines.")
