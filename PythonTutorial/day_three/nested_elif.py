
print("Welcome to the rollercoaster!")

height = int(input("How tall are you in centimeters? "))
adult_price = "$12"
teenage_price = "$7"
child_price = "$5"

if height >= 120:
  age = int(input("How old are you? "))
  if age > 18:
    print(f"You may purchase a ticket for {adult_price}")
  elif age >= 12 and age <= 18:
    print(f"You may purchase a ticket for {teenage_price}")
  else:
    print(f"You may purchase a ticket for {child_price}")
else:
  print("I'm sorry, but you cannot purchase a ticket due to being too short.")