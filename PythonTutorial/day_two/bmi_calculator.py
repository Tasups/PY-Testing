print("Calculate your BMI")

height = input("Please enter your height in meters: ")

weight = input("Please enter your weight in kg: ")

bmi_float = float(weight) / float(height) ** 2

bmi_int = int(bmi_float)

print("Your BMI is " + str(bmi_int))

