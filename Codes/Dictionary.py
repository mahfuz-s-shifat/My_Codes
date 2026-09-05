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




empty_dic = {} # Creating an empty dictionary

empty_dic["name"] = "Alif" # Adding a key-value pair to the empty dictionary
empty_dic["age"] = 20
empty_dic["major"] = "Computer Science"
empty_dic["gpa"] = 3.8
print(empty_dic)

empty_dic.update({
    "country": "Bangladesh",  # Adding multiple key-value pairs to the dictionary using the update() method
    "city": "Dhaka",
    "grade": "A+"
})

print(empty_dic)

print(student.keys()) # Output: dict_keys(['name', 'age', 'major', 'gpa'])

print(student.items()) # Output: dict_items([('name', 'Alif'), ('age', 20), ('major', 'Computer Science'), ('gpa', 3.8)])

for key, value in student.items(): # Iterating through the dictionary using a for loop
    print(key, ":", value)

del empty_dic["country"] # Deleting a key-value pair from the dictionary using the del statement
empty_dic.pop("gpa") # Deleting a key-value pair from the dictionary using the pop() method
empty_dic.pop("cities", None) # Deleting a key-value pair from the dictionary using the pop() method with a default value to avoid KeyError

print(empty_dic)







