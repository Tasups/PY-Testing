# TIP CALCULATOR

print("Welcome to the tip calculator.")

bill_total = float(input("What was the total bill? $"))

split_num = int(input("How many will split the bill? "))

tip_percentage = int(input("What percentage tip would you like to give? 10, 12, 15, etc.? %"))

bill_split = bill_total / split_num

split_and_tip = round(bill_split + (bill_split * tip_percentage / 100), 2)

# note this as it is a format method, we previously had just a round function above
amount_to_pay = "{:.2f}".format(split_and_tip)

print(f"Each person should pay: ${str(amount_to_pay)}")