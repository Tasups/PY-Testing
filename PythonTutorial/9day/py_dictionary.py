programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "The action of doing something over and over again",
}

# To access parts of a dictionary

# this prints out the value for bug in the programming_dictionary
# print(programming_dictionary["Bug"])

# this is how to add something to a dictionary, use the key name you want to use and assign it to the value you want to use
programming_dictionary["Python"] = "A very popular programming language."

# print(programming_dictionary)

# this is how to edit an entry in a dictionary
# programming_dictionary["Python"] = "A type of snake that can get quite large."

# print(programming_dictionary)

# this is how to create an empty dictionary
new_dictionary = {}

# this is how to wipe a dictionary
# programming_dictionary = {}


# this is how to loop through a dictionary getting the keys
# for key in programming_dictionary:
#   print(key)
  
# this is how to loop through a dictionary getting the values
for value in programming_dictionary:
  print(f"{value} : {programming_dictionary[value]}")
  