import math

# 1.Display numbers from -10 to -1 using for loop
# 2. Use else block to display a message “Done” after successful execution of for loop
for i in range(-10, 0):
    print(i)
    if i == -1:
        print("Done")
        
print("===================")
# 3.Write a program to display all prime numbers within a range
def isPrime(n: int) -> bool:
    if n < 1:
        return False
    elif n == 1:
        return True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

for i in range(20):
    p = ""
    if isPrime(i):
        p = "Prime"
    else:
        p = "Not Prime"
    print("{0} = {1}".format(i, p))
    
print("===================")
# 4.Use a loop to display elements from a given list present at odd index positions
arr = [2,4,6,8,10,12,14,16,18,20]
for i in range(len(arr)):
    if i % 2 != 0:
        print(arr[i])
        
print("===================")
# 5. Display numbers from a list using loop
# a. The number must be divisible by five
for i in arr:
    if i % 5 == 0:
        print(i)

print("===================")
# b. If the number is greater than 150, then skip it and move to the next number
numbers = [12, 75, 150, 180, 145, 525, 50]
skipped = False
for i in numbers:
    if not skipped and i > 150:
        skipped = True
        continue
    print(i)
    
print("===================")
# c. If the number is greater than 500, then stop the l
for i in numbers:
    if i > 500:
        break
    print(i)