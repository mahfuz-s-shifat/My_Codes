name = input("Enter your name: ")

file = open("name.txt", "w")

file.write(name)

file.close()

print("Name saved successfully")