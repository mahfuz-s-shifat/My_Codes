# Problem 01 -> Student Grade Calculator

student_name = input("Enter student name: ")
mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))

total_marks = mark1 + mark2 + mark3
average_marks = total_marks / 3

if 80 <= average_marks <= 100:
    grade = "A+"
elif 70 <= average_marks < 80:
    grade = "A"
elif 60 <= average_marks < 70:
    grade = "B"
elif 50 <= average_marks < 60:
    grade = "C"
else:
    grade = "F"

print(f"Student Name: {student_name}")
print(f"Total Marks: {total_marks}")
print(f"Average: {average_marks}")
print(f"Grade: {grade}")





# Problem 02 ->  Simple Shopping Cart

customer_name = input("Enter Customer Name: ")

product1 = input("Enter Product 1: ")
price1 = float(input("Enter Price: "))

product2 = input("Enter Product 2: ")
price2 = float(input("Enter Price: "))

product3 = input("Enter Product 3: ")
price3 = float(input("Enter Price: "))

subtotal = price1 + price2 + price3

if subtotal >= 5000:
    discount = subtotal * 0.20   # 20% discount
elif subtotal >= 3000:
    discount = subtotal * 0.10   # 10% discount
elif subtotal >= 1000:
    discount = subtotal * 0.05   # 5% discount
else:
    discount = 0                 # No discount

final_total = subtotal - discount

print()
print(f"Customer Name: {customer_name}")
print(f"Product 1: {product1}")
print(f"Price: {price1}")
print(f"Product 2: {product2}")
print(f"Price: {price2}")
print(f"Product 3: {product3}")
print(f"Price: {price3}")
print(f"Subtotal: {subtotal}")
print(f"Discount: {discount}")
print(f"Final Total: {final_total}")







