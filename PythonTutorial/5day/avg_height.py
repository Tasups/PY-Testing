print("The Height Calculator!")

heights = input("Input a list of heights in centimeters:\n").split()

total_height = 0
heights_length = 0

for height in heights:
  height_int = int(height)
  total_height += height_int
  heights_length += 1
  
# This is a way that is used to separate person for length and height for total height, weird.
# for person in heights: 
#   num_person += 1
  
average_height = int(total_height / heights_length)

print(total_height)

print(f"The average height of the heights listed is {average_height}")

# 156 178 165 171 187