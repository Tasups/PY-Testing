# welcome to pizza thing
# size = s,m,l
# small 15
# medium 20
# large 25
# pepperoni for small 2
# pepperoni for large 3
# extra_cheese for any size 1

print("Welcome to the Pizza Place!")
size = input("What size pizza would you like? Small(S), Medium(M), or Large(L)? ")
pepperoni = input("Would you like pepperoni on your pizza(Y or N)? ")
extra_cheese = input("Would you like extra cheese on your pizza(Y or N)? ")
total = 0

# size control
if size == 'S':
  total += 15
elif size == 'M':
  total += 20
elif size == 'L':
  total += 25

# pepporoni control
if pepperoni == 'Y':
  if size == 'S':
    total += 2
  else:
    total += 3

# extra cheese control
if extra_cheese == 'Y':
  total += 1
  
print(f"The total for your pizza comes to ${total}")