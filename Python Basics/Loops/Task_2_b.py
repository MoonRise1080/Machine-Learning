"""
b.
*
**
***
****

"""

i = 1
while i <= 4:
    j = 1
    while j <= i:
        print("*", end = "")
        j += 1
    i += 1
    print("")