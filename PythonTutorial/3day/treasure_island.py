print("Welcome to Treasure Ilsand! Find the treasure to win!")

which_direction = input("You come to a fork in the road. Do you go [left] or [right]? ").lower()

if which_direction == "left":
  swim_or_wait = input("After several hours following the trail, you come upon a large lake. Do you [swim] or [wait] for a boat? " ).lower()
  if swim_or_wait == "wait":
    which_door = input("You get on the boat and it takes you to the other side of the lake. Upon the shore is the house you've been looking for. You go inside and are immediately confronted with three doors, which do you choose? [blue], [red], or [yellow]? ").lower()
    if which_door == "yellow":
      print(f"You open the {which_door} door. You've made it to the treasure chamber of Treasure Island!\nYou Win!!!")
    else:
      print(f"You open the {which_door} door and find yourself falling into darkness.\nYou lose.")
  else:
    print("You struggle to swim as hard as you can but your body finally gives out and you drown.\nYou lose.")
else:
  print("You were hit with several darts and sleep into eternity.\nYou lose.")