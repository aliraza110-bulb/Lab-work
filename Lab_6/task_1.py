# Task #1 
# Scenario: A school wants to automate the calculation of final grades for
#  students based on their quiz, assignment, and exam scores. You have been asked to 
# write a Python function called calculate_final_grade() that takes three parameters:
# quiz_score (out of 25)
# assignment_score (out of 35)
# exam_score (out of 40)
# The function should return the final grade as the sum of these scores.
# Additionally, write another function grade_category() that takes the final grade
#  as input and returns:
# "A" if the score is 85 or above
# "B" if the score is 70 to 84
# "C" if the score is 50 to 69
# "F" if the score is below 50
# Task Description: Write a Python program that asks the user to enter their quiz
# , assignment, and exam scores, calculates the final grade using calculate_final_grade(), 
# determines the grade category using grade_category(), and displays the result.

def calculate_final_grade(quiz,assignment,exam):
    return quiz+assignment+exam

def grade_category(final_grade):

    if final_grade >= 85:
        return(" A grade")
    elif final_grade >=70:
        return("B grade")
    elif final_grade >=50:
        return("C grade")
    else:
        return("Fail")

quiz=float(input("Enter quiz score (out of 25 )"))
assignment=float(input("Enter assignment score (out of 35 )"))
exam=float(input("Enter exam score (out of 40)"))

final_grade=calculate_final_grade(quiz,assignment,exam)
category=grade_category(final_grade)

print(f"Final grade :{final_grade}\nCategory:{category}")