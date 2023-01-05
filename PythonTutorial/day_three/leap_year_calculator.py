# on every year that is evenly divisible by 4
# except every year that is evenly divisible by 100
# unless the year is also evenly divisible by 400

print("This is a leap year calculator.")

year = int(input("Please put in the year: "))

if year % 4 == 0:
  if year % 100 != 0:
    print("It is a leap year.")
  else:
    if year % 400 == 0:
      print("It is a leap year")
    else:
      print("Not a leap year.")
else:
  print("Not a leap year.")