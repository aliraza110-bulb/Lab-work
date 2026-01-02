# Scenario: A cybersecurity team is developing a program to detect and 
# extract secure passwords from a system log. A valid password must meet 
# strict security guidelines to prevent hacking attempts.
# Secure Password Requirements:
# Must be 8 to 16 characters long
# Must contain at least one uppercase letter (A-Z)
# Must contain at least one lowercase letter (a-z)
# Must contain at least one digit (0-9)
# Must contain at least one special character (@, #, $, %, &, etc.)
# 🔹 Examples of Valid Passwords:
# ✅ Secure@123
# ✅ Xy#9klPz!
# ❌ password123 (missing special character)
# ❌ HELLO@WORLD (missing digit)
# ❌ abc123! (too short)
# You’re Task:
# Write a Python function validate_password(password) that:
# Uses RegEx to check if the password follows the correct security rules.
# Returns "Valid Password" if correct, otherwise "Invalid Password".
# Write a Python program that:
# Takes a list of passwords as input.
# Uses validate_password() to check each password.
# Prints only the valid passwords.

import re

def validate_password(password):
    pattern = (
        r'^(?=.*[A-Z])'
        r'(?=.*[a-z])'
        r'(?=.*\d)'
        r'(?=.*[@#$%&!])'
        r'[A-Za-z\d@#$%&!]{8,16}$'
    )
    if re.match(pattern, password):
        return "Valid Password"
    else:
        return "Invalid Password"


passwords = [
    "Secure@123",
    "Xy#9klPz!",
    "password123",
    "HELLO@WORLD",
    "abc123!"
]

for pwd in passwords:
    if validate_password(pwd) =="Valid Password":
        print("\n Valid passwords",pwd)