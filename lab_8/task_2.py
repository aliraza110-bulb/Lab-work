# Task #2
# Scenario: A bank security system needs to verify and extract
# valid account numbers from customer records. 
# The account numbers must follow a specific pattern to ensure they belong to the bank.
#  Account Number Format:
# Starts with "ACC"
# Followed by exactly 2 uppercase letters
# Ends with exactly 5 digits
# 🔹 Examples of Valid Account Numbers:
# ✅ ACCAB12345
# ✅ ACCMN67890


import re

def validate_account_number(account):
    pattern=r"^ACC[A-Z]{2}\d{5}$"
    if re.match(pattern,account):
        return "Valid Account"
    else:
        return "Invalid Account"
    
accounts=[
    "ACCAB12345",
    "ACCMN67890"
]

for acc in accounts:
    if validate_account_number(acc) == "Valid Account":
        print(acc)


text = """
Customer data includes ACCAB12345 and ACCMN67890.
Invalid entries like ACCabc12345 and ACCX1234 should be ignored.
"""

pattern=r"ACC[A-Z]{2}\d{5}"

valid_account=re.findall(pattern,text)

print("\nExtracted account numbers")
for acc in valid_account:
    print(acc)