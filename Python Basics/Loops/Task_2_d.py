"""
d.
1
1 3
1 3 5
1 3 5 7

"""

i = 1
k = 1

while i <= 4:
    j = 1
    while j <= i:
        print((2 * j) - 1, end = " ")
        j += 1
        k += 1
    i += 1
    print("")