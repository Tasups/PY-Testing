import random

print("Welcome to rock, paper, scissors.")

rock = '''
        ____
    ---' ___)__
          (____)
          (____)
          (___)
     ---.(___)
  '''

paper = '''
        _______
    ---'  _____)____
            ________)
            _________)
          _________)
    ---.________)
  '''

scissors = '''
        ____
    ---' ___)_____
          ________)
          ________)
         (____)
    ---.(___)
  '''

user_sel = input("What do you choose? 'Rock', 'Paper', or 'Scissors'? ").lower()

if user_sel == 'paper':
  print(paper)
elif user_sel == 'rock':
  print(rock)
elif user_sel == 'scissors':
  print(scissors)

comp_sel = random.randint(0,2)

if comp_sel == 0:
  print(f"Computer chose:\n{rock}")
elif comp_sel == 1:
  print(f"Computer chose:\n{paper} ")
elif comp_sel == 2:
  print(f"Computer chose:\n{scissors}")

# User chooses rock 
if user_sel == 'rock' and comp_sel == 0:
  print("It's a draw.")
elif user_sel == 'rock' and comp_sel == 1:
  print("You lose.")
elif user_sel == 'rock' and comp_sel == 2:
  print("You win!")
  
# User chooses paper
if user_sel == 'paper' and comp_sel == 0:
  print("You win!")
elif user_sel == 'paper' and comp_sel == 1:
  print("It's a draw.")
elif user_sel == 'paper' and comp_sel == 2:
  print("You lose.")
  
# User chooses scissors
if user_sel == 'scissors' and comp_sel == 0:
  print("You lose.")
elif user_sel == 'scissors' and comp_sel == 1:
  print("You win!")
elif user_sel == 'scissors' and comp_sel == 2:
  print("It's a draw.")
