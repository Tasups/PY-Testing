
def is_leap(year):
  """determines if the year input is a leap year and returns true if it is and false if it is not"""
  if year % 4 == 0:
    if year % 100 != 0:
      return True
    else:
      if year % 400 == 0:
        return True
  else:
    return False

def days_in_month(year, month):
  total = 0
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  
  if is_leap(year) == True and month == 2:
    total += 1
  
  total += month_days[month - 1]
  return total
  
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)