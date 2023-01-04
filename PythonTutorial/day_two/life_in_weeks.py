print("How much time do you have until 90 years old?")

years = int(input("How many years old are you? "))

years_left = 90 - years

weeks_left = years_left * 52

months_left = years_left * 12

days_left = round(years_left * 365.21)

print(f"You have {days_left} days, {weeks_left} weeks, {months_left} months left.")