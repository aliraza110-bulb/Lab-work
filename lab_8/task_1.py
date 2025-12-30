# Task #1
# Scenario: A company HR department needs a program to extract and validate 
# employee ID numbers from a list. Each employee ID follows this format:
#  Employee ID Format:
# Starts with "EMP"
# Followed by exactly 4 digits (e.g., EMP1234)
# You’re Task:
# Write a Python function validate_employee_id(emp_id) that:
# Uses RegEx to check if the ID follows the correct format.
# Returns "Valid ID" if correct, otherwise "Invalid ID".
# Write a Python program that:
# Takes a list of employee IDs as input.
# Uses validate_employee_id() to check each ID.
# Prints only the valid employee IDs.

import re

def validate_employee_id(emp_id):
    pattern=r"^EMP\d{4}$"
    if re.match(pattern,emp_id):
        return "Valid Id"
    else:
        return "Invalid Id"
    
emp_ids=[
    "EMP1234",
    "EMP5678",
    "EMP12",
    "emp1234",
    "EMP12345"
]

for em_id in emp_ids:
    if validate_employee_id(em_id) == "Valid Id":
        print(em_id)