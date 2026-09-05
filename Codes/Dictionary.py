student = {
    "name": "Alif", # Pair of key and value
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}

data = {
    "name": ["Alif", "Tuhin", "Asif"], # Pair of key and value
    "age": [20, 21, 22],
    "major": ["Computer Science", "Mathematics", "Physics"],
}

print(data)

data["gpa"] = [4.0, 3.8, 3.5] # Adding a new key-value pair to the dictionary
print(data)


print()

print(data["name"]) # Accessing the value associated with the key "name"
print(data["age"]) # Accessing the value associated with the key "age"
print(data["major"]) # Accessing the value associated with the key "major"
print(data["gpa"]) # Accessing the value associated with the key "gpa"


dic = {
    "a" : [1,2,3,4,5],
    "a" : [6,7,8,9,10]  # This will overwrite the previous value associated with the key "a"
}

print(dic) # Output: {'a': [6, 7, 8, 9, 10]}
