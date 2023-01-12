import random

print("This is a password generator")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ask for how many of each type the user wants
num_letters = int(input("How many letters do you want in your password? "))
num_numbers = int(input("How many numbers do you want in your password? "))
num_symbols = int(input("How many symbols do you want in your password? "))

# the password stored
password = ''

# get the sum of the characters to go in the password to know how to construct the password by length
password_length = num_letters + num_numbers + num_symbols

# store the chars to use
chars = []

# iterate over each type for the number of times asked for each type and store each in a list
for n in range(0, num_letters):
  letter_rand_index = random.randint(0, len(letters) - 1)
  chars.append(letters[letter_rand_index])
for n in range(0, num_numbers):
  num_rand_index = random.randint(0, len(numbers) - 1)
  chars.append(numbers[num_rand_index])
for n in range(0, num_symbols):
  symbol_rand_index = random.randint(0, len(symbols) - 1)
  chars.append(symbols[symbol_rand_index])

# shuffle the order in chars
random.shuffle(chars)

# put password into string
password = "".join(str(x) for x in chars)

# THIS IS ME TRYING TO WRITE SHUFFLE FOR PYTHON!
# store the index numbers where a char has been pulled from
# index_visited = []

# for n in range(0, len(chars)):
#   index_target = random.randint(0, len(chars))
#   index_visited.append(index_target)
#   for i in index_visited:
#     if i not in 

# use random.int for the number of characters in the password and pull from one type until that type is
# empty

print(password)