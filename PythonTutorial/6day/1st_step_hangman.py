
import random
from word_list import words
from stages import stages

chosen_word = random.choice(words)

print(f"The solution is: {chosen_word}")

display = []

for letter in chosen_word:
  display.append("_")
  
player_lives = 6

letters_guessed = []

while "_" in display and player_lives != 0:
  guess = input("Guess a letter: ").lower()
  
  if guess in letters_guessed:
    print("You've already guessed that letter. Please guess again.")
    
  if guess not in letters_guessed:
    current_result = ""
    letters_guessed.append(guess)
    for position in range(len(chosen_word)):
      letter = chosen_word[position]
      if letter == guess:
        display[position] = letter
        current_result = " ".join(display)
    print("\n")
    print(current_result)
    print('''\n________________''')
    
    if guess not in chosen_word and guess not in letters_guessed:
      player_lives -= 1
      if player_lives == 0:
        print(stages[player_lives])
        print("You lose!")
      else:
        print("______________")
        print("Your guess was wrong. Please try again.")
        print(stages[player_lives])
  
if player_lives > 0:  
  result = "".join(display)
  print(f"The solution is {result}\nYou won!")

# index = 0

# for letter in chosen_word:
#   if guess == letter:
#     display[index] = guess
#     index += 1
#   else:
#     print(f"Wrong at index: {index}")
#     index += 1