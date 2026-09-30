# Problem 01 - Current Date and Time

from datetime import datetime

current_datetime = datetime.now()

print("Current Date and Time:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))





"""

Problem 02 - Write a Python program that creates a Python dictionary containing a student's
name, age, and department. Then convert the dictionary into a JSON string using the json
module and print it.

"""

import json

student = {
    "name": "Rahim",
    "age": 20,
    "department": "CSE"
}

student_json = json.dumps(student)

print(student_json)