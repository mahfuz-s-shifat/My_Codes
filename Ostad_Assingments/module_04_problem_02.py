import json

student = {
    "name": "Rahim",
    "age": 20,
    "department": "CSE"
}

student_json = json.dumps(student)

print(student_json)