"""
c.
1
2 2
3 3 3 
4 4 4 4 

"""

i = 1
while i <= 4:
    j = 1
    while j <= i:
        print(i, end = " ")
        j += 1
    i += 1
    print("")