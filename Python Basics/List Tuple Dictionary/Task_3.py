"""
Task 3: Dictionaries
Write a program that:
Creates a dictionary where keys are subject names (e.g., Math, Science) and values are the marks (e.g., 90, 85).
Adds a new subject with its mark to the dictionary.
Updates the mark for one subject.
Prints the average marks.

"""

subjects = [
    {"name" : "Math", "mark" : 99},
    {"name" : "Science", "mark" : 90}
]

print(subjects)

subjects.append({"name" : "English", "mark" : 100})
print(subjects)

subjects[0]['mark'] = 100
print(subjects)

for x in subjects:
    print(f"Subject: {x['name']} Marks: {x['mark']}")
