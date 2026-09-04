while True:

    n = int(input("\nEnter Last number or 0 to exit: "))

    if n == 0:
        break

    sum = 0

    for x in range(1, n + 1, 1):
        sum += x

    print("Sum of numbers from 1 to", n, "is:", sum)