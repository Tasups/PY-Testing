# Step 1 Hangman Project

import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f"The solution is: {chosen_word}")

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter: ").lower()

# TODO-3 - Check if the letter the user guessed is one of the letters in the chosen_word

for letter in chosen_word:
  if guess == letter:
    print("Right")
  else:
    print("Wrong")