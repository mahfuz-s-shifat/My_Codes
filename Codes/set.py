# Set {}
# Immutable, unordered, unindexed collection of unique elements
# No duplicate elements allowed

a = [11, 11, 90, 67, 23, 25, 34, 45, 56, 67, 78, 89, 90]
s = set(a)

print(s)


# Intersection & Union

x = {1, 2, 3, 4, 5}
y = {4, 5, 6, 7, 8}

print(x & y)  # Intersection
print(x | y)  # Union

print(">>>---------------------------------<<<")

print(x.intersection(y))  # Intersection
print(x.union(y))  # Union