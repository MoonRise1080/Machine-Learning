"""
Write a program that:
Creates a list of 5 numbers.
Adds a new number to the list.
Removes the second number from the list.
Prints the sum of all numbers in the list.

"""

arr = [1, 2, 3, 4, 5]

arr.append(10)

arr.remove(arr[1])

sum = 0
for x in arr:
    sum += x

print(arr)
print(sum)