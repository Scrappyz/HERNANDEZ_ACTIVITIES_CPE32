# Exercise 6

# Find max of 3 numbers
print(max(5, 10, 1))

# Get sum of all numbers in list
print(sum((5, 10, 9, 2)))

# Reverse a string
s = "Hello World"[::-1]
print(s)

# Count number upper and lowercase letters
count_lower = 0
count_upper = 0
for i in s:
    if i.isupper():
        count_upper += 1
    elif i.islower():
        count_lower += 1
print("Lowercase: " + str(count_lower))
print("Uppercase: " + str(count_upper))

# Return distinct elements
l = [2, 6, 2, 3, 1, 1, 4, 4, 4]
l = list(set(l))
print(l)