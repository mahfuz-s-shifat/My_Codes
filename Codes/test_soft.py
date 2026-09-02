x = int(input("Enter your roll number: "))

r1, r2, r3, r4, r5 = 101, 102, 103, 104, 105
n1, n2, n3, n4, n5 = "Fahim" , "Noyon" , "Anik" , "Alif" , "Abir"
re1, re2, re3, re4, re5 = "CGPA 3.16", "CGPA 3.57", "CGPA 3.85", "CGPA 3.92", "CGPA 3.98"


if x == r1:
    print("Your name : ", n1)
    print("Your result : ", re1)
elif x == r2:
    print("Your name : ", n2)
    print("Your result : ", re2)
elif x == r3:
    print("Your name : ", n3)
    print("Your result : ", re3)
elif x == r4:
    print("Your name : ", n4)
    print("Your result : ", re4)
elif x == r5:
    print("Your name : ", n5)
    print("Your result : ", re5)
else:
    print("Roll number not found.")
