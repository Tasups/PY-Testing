
current_value = 0

def calculate(first_int, operator, second_int):
  if operator == "+":
    current_value = first_int + second_int
  elif operator == "-":
    current_value = first_int - second_int
  elif operator == "*":
    current_value = first_int * second_int
  elif operator == "/":
    current_value = first_int / second_int
  
  print(f"{first_int} {operator} {second_int} = {current_value}")


go_again = ""
counter = 0

def start_calculating(current_value, go_again, counter):
  
  if go_again == "n" or counter == 0:
    first_num = int(input("Please enter your first number: "))
    operator = input("Select the operator, + - * / :")
    second_num = int(input("Please enter your second number: "))
  elif go_again == "y" or counter > 0:
    operator = input("Select the operator, + - * / :")
    second_num = int(input("Please enter your second number: "))
    
  calculate(first_num, operator, second_num)
  
  go_again = input(f"Type 'y' to continue calculating with {current_value}, or type 'n' to start a new calculation: ")
  
  if go_again == "y":
    counter += 1
    start_calculating(current_value, go_again, counter)
  if go_again == "n":
    counter = 0
    current_value = 0
    start_calculating(current_value, go_again, counter)
    
    
start_calculating(current_value, go_again, counter)