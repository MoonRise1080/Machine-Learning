"""
Task 2: Tuples
Write a program that:
Creates a tuple with the names of 5 cities.
Prints the third city in the tuple.
Converts the tuple into a list, adds a new city, and converts it back to a tuple.
Prints the modified tuple.

"""

city = ("Dhaka", "Rajshahi", "Sylhet", "Khulna", "Borishal")

print(city)

list_city = list(city)

list_city.append("Chittagong")

city = tuple(list_city)

print(city)
