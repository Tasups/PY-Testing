# Place a treasure in a specific place using COLUMN AND ROW coords in that order

row1 = ["😆","😆","😆"]
row2 = ["😆","😆","😆"]
row3 = ["😆","😆","😆"]

treasure = "💰"

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}\n")

position = input("Where do you want to put the treasure? ")

# split_position = position.split(" ")

# row = int(split_position[0])
# column = int(split_position[1])

row = int(position[1]) - 1
column = int(position[0]) - 1

map[row][column] = treasure

print(f"{row1}\n{row2}\n{row3}\n")