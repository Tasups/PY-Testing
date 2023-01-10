print("This is a password generator")

letters = []
numbers = []
symbols = []

# ask for how many of each type the user wants
num_letters = int(input("How many letters do you want in your password? "))
num_numbers = int(input("How many numbers do you want in your password? "))
num_symbols = int(input("How many symbols do you want in your password? "))

# get the sum of the characters to go in the password to know how to construct the password by length
password_length = num_letters + num_numbers + num_symbols

# iterate over each type for the number of times asked for each type and store each in a list

# use random.int for the number of characters in the password and pull from one type until that type is
# empty