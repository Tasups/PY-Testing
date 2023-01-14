# Step 1 Hangman Project

import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f"The solution is: {chosen_word}")

display = []

for letter in chosen_word:
  display.append("_")
  
print(display)

#while letter in display == "_":
guess = input("Guess a letter: ").lower()

index = 0

# for letter in chosen_word:
#   if guess == letter:
#     display[index] = guess
#     index += 1
#   else:
#     print(f"Wrong at index: {index}")
#     index += 1
    
# Alternate for loop to put in the letter
for position in range(len(chosen_word)):
  letter = chosen_word[position]
  if letter == guess:
    display[position] = letter

    
print(display)