# Paint calculator
import math

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

def paint_calc(height = test_h, width = test_w, cover = coverage):
  result = (height * width) / cover
  print(f"You will need to buy {math.ceil(result)} cans of paint.")
  
paint_calc(test_h, test_w, coverage)