# Grading exercise

# Write code to dynamically create a new dictionary that transforms the numeric grades to the following
# Score 91-100 => "Outstanding"
# Score 81-90 => "Exceeds Expectations"
# Score 71-80 => "Acceptable"
# Score 61-70 => "Fail"


student_scores = {
  "Harry": 81,      # Exceeds Expectations
  "Ron": 78,        # Acceptable
  "Hermione": 99,   # Outstanding
  "Draco": 74,      # Acceptable
  "Neville": 62,    # Fail
}

# start empty dictionary
student_grades = {}

# iterate over the student_scores dictionary and transforms the value to a corresponding grade above such that Harry: Exceeds Expectations, Hermione: Outstanding, etc.

for student in student_scores:
  if student_scores[student] > 90:
    student_grades[student] = "Outstanding"
  elif student_scores[student] > 80:
    student_grades[student] = "Exceeds Expectations"
  elif student_scores[student] > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"
    
print(student_grades)