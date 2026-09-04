# Grading System

while True:
    marks = int(input("\nEnter your marks (0-100): "))
    if marks < 0 or marks > 100:
        print("Invalid marks. Please enter a value between 0 and 100.")
        continue
    elif marks >= 90:
        print("Grade: A+")
    elif marks >= 80:
        print("Grade: A")
    elif marks >= 70:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    elif marks >= 50:
        print("Grade: D")
    elif marks >= 40:
        print("Grade: E")
    else:
        print("Grade: F")
        