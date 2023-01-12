print("This is a BMI calculator.")

height = float(input("What is your height in meters? "))
weight = float(input("What is your weight in kilograms? "))

bmi = round(weight / height ** 2, 2)

if bmi < 18.5:
  print(f"Your BMI is {bmi} are underweight")
elif bmi > 18.5 and bmi <= 25:
  print(f"Your BMI is {bmi} are at a normal weight")
elif bmi > 25 and bmi <= 30:
  print(f"Your BMI is {bmi} are overweight")
elif bmi > 30 and bmi <= 35:
  print(f"Your BMI is {bmi} are obese")
else:
  print(f"Your BMI is {bmi} are clinically obese")