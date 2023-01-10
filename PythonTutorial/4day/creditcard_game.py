import random

print("God help us, we're going to play the credit card game. ")

players = input("Who's throwing their card in the ring?!! ")

player_list = players.split(", ")

random_index = random.randint(0, len(player_list))

print(player_list[random_index])