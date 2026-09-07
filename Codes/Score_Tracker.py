students = {}

while True:
    name = input("Enter student name: ").strip()
    
    if name.lower() == 'stop':
        break
    
    try:
        score = int(input("Enter score: "))
        students[name] = score
    except ValueError:
        print("Please enter a valid numeric score.")

