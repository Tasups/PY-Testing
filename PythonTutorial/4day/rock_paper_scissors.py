import random

print("Welcome to rock, paper, scissors.")

user_sel = input("What do you choose? 'Rock', 'Paper', or 'Scissors'? ").lower()

if user_sel == 'paper':
  print('''
        _______
    ---'  _____)____
            ________)
            _________)
          _________)
    ---.________)
  ''')
elif user_sel == 'rock':
  print('''
        __
    ---'  )
    
  ''')

comp_sel = random.randint(0,2)
print(comp_sel)

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
