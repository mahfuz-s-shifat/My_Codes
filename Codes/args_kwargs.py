def add(*numbers):    # *args
    total = 0
    for n in numbers:
        total = total+n
    return total

print(add(50, 50, 50, 50, 50, 50, 50, 50))




def information(**details):     # **kwargs
    print(details)

information(name = "Anik", age = 25, city = "Dhaka", country = "Bangladesh", gmail = "anikkhan@gmail.com")