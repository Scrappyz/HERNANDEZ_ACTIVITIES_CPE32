# Exercise 7
"""1. Write a Python program to create an array of 3 integers and display the array items. 
Access individual elements through indexes."""
arr = [1, 3, 5]
for i in arr:
    print(i)

print("===============")
"""2. Write a Python program to append a new item to the end of the array."""
print("Original array: array('i', {0})".format(arr))
print("Append 11 at the end of the array:")
arr.append(11)
print("New array: array('i', {0})".format(arr))

print("===============")
"""3. Write a Python program to reverse the order of the items in the array."""
print("Original array: array('i', {0})".format(arr))
print("Reverse the order:")
arr.reverse()
print("New array: array('i', {0})".format(arr))

print("===============")
"""4. Write a Python program to find out if a given array of integers contains any duplicate elements. 
Return true if any value appears at least twice in the array, and return false if every element is distinct."""
def hasDuplicate(arr: list) -> bool:
    unique = set()
    for i in arr:
        if i in unique:
            return True
        else:
            unique.add(i)
    return False

print(hasDuplicate([1, 2, 3, 4, 1]))
print(hasDuplicate([2, 6, 7, 4, 8]))
print(hasDuplicate([110, 8, 99, 658]))

print("===============")
"""5.Write a Python program to find the first duplicate element in a given array of integers. 
Return -1 if there are no such elements."""
def firstDuplicate(arr: list) -> int:
    unique = set()
    for i in arr:
        if i in unique:
            return i
        else:
            unique.add(i)
    return -1

print(firstDuplicate([1, 2, 3, 4, 1]))
print(firstDuplicate([2, 6, 7, 4, 8]))
print(firstDuplicate([110, 8, 99, 658, 8, 99]))