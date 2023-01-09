
print("This is a totally legit TRUE LOVE calculator.")

name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()

combined_names = name1 + name2
name_to_lower = combined_names.lower()

t = name_to_lower.count("t")
r = name_to_lower.count("r")
u = name_to_lower.count("u")
e = name_to_lower.count("e")

l = name_to_lower.count("l")
o = name_to_lower.count("o")
v = name_to_lower.count("v")
e = name_to_lower.count("e")

true = t + r + u + e
love = l + o + v + e

love_score = int(str(true) + str(love))


if (love_score < 10) or (love_score > 90):
  print(f"Your score is {love_score}. You go together like Coke and Mentos!")
elif (love_score > 40) and (love_score < 50):
  print(f"Your score is {love_score}. You are alright together.")
else:
  print(f"Your score is {love_score}.")