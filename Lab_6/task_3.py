# Task #3
# Scenario: You are creating a grading system for a school. 
# The system should calculate a final grade based on multiple assessments (assignments, quizzes, exams), 
# with each assessment having a different weight. How would you implement this?
#  Objective: Develop a grading system that calculates final grades based on weighted assessments.
# Instructions:
# Create a function named calculate_final_grade that takes three parameters: assignments, quizzes, and exams.
# Define weights for each assessment type (e.g., 40% for assignments, 20% for quizzes, and 40% for exams).
# Compute the final grade using the provided weights.
# Return the final grade rounded to two decimal places.


def calculate_final_grade(assignments,quizzes,exams):
    final_grade=(assignments*0.4)+(quizzes*0.2)+(exams*0.4)
    return round(final_grade,2)


assignment_score=80
quiz_score=70
exam_score=90

final_grade=calculate_final_grade(assignment_score,quiz_score,exam_score)
print("The final grade is",final_grade)
