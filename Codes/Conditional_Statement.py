pass_mark = int(input("Enter your pass mark: "))

if pass_mark >= 40:
    print("You have passed the exam.")
else:
    print("You have failed the exam.")


# Grading System

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Your Grade Is A+.")
elif marks >= 80:
    print("Your Grade Is B.")
elif marks >= 60:
    print("Your Grade Is C.")
elif marks >= 50:
    print("Your Grade Is D.")
elif marks >= 40:
    print("Your Grade Is E.")
elif marks > 100 and marks < 0:
    print("Invalid Marks. Please enter a valid marks.")
else:
    print("Your Grade Is F. You have failed the exam.")