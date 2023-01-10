print("This finds the highest score in the list.")

student_scores = input("Input a list of student scores:\n").split()

highest_score = 0
total_score = 0
student_scores_len = 0

for score in student_scores:
  score_int = int(score)
  if score_int > highest_score:
    highest_score = score_int
  total_score += score_int
  student_scores_len += 1
    
average_score = total_score / student_scores_len
print(f"The highest score in the class is {highest_score}")
print(f"The average score in the class is {average_score}")