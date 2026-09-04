""" 

# Demonstrating the range function 

a = list(range(0, 10))
a2 = list(range(10))
b= tuple(range(0, 10))
c = list(range(0, 10, 2))

# range(start, end, step)  # start: starting number, end: ending number, step: step size

"""


for x in range(0, 10):
    if x % 2 == 0:
        print(x, "is even")
    else:
        print(x, "is odd")