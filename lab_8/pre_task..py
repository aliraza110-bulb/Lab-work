# Procedure:
# A university admissions office needs a program to extract and validate student email addresses from a list of applications. The university follows a strict email format:
# Email format: studentID@university.edu
# studentID must be a 6-digit number
# Domain must be "@university.edu"
# You’re Task:
# Write a Python function validate_email(email) that:
# Uses RegEx to check if the email follows the correct format.
# Returns "Valid Email" if correct, otherwise "Invalid Email".
# Write a Python program that:
# Takes a list of student emails as input.
# Uses validate_email() to check each email.
# Prints only the valid emails

import re

def validate_email(email):
    pattern=r'^\d{6}@university\.edu$'
    if re.match(pattern,email):
        return "Valid Email"
    else:
        return "Invalid email"
    
emails=[
    "123456@university.edu",
    "654321@university.edu",
    "12345@university.edu",
    "abc123@university.edu",
    "123456@gmail.com"
]

for email in emails:
    if validate_email(email)=="Valid Email":
        print(email)