"""Python program find difference between each number in the array and the average of all numbers"""
arr = [8,6,7,5,9,6,11,4,1,12,20]
sum = arr[0]
for i in range(1, len(arr)):
    print(arr[i] - arr[i-1])
    sum = sum + arr[i]
print("Average: {0}".format(sum / len(arr)))

print("=================")
"""Python program to convert a string in an array"""
s = "1,2,3,4,5"
print(s.split(","))

print("=================")
"""Python program to split an array in two and store even numbers in one array and odd numbers in the other."""
odd = []
even = []
for i in arr:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Array: {0}".format(arr))
print("Odd: {0}".format(odd))
print("Even: {0}".format(even))

print("=================")
"""Python program to perform insertion sort on an array."""
def insertionSort(arr: list):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            j = j-1
        
print("Original array: {0}".format(arr))
insertionSort(arr)
print("Sorted array: {0}".format(arr))