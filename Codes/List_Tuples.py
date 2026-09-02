a = [1,2,3,4,5, "Fahim", "Ali", "Ahmed" , 5.2, 6.3, 7.4, 8.5, 9.6, 10.7]

a[2] = 99 # Change the value at index 2
print(a) # Print the modified list
print(a[-5]) # Print the value at index -5 (5th element from the end)

x = "hello"
print(list(x)) # Print the list of characters in the string

a.append("Anik")
a.index("Anik") # Find the index of the newly appended element
a.remove("Fahim") # Remove the element "Fahim" from the list

print(a) # Print the list after appending a new element
