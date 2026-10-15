"""EXERCISE 8"""

"""Create a list of dictionaries for 5 students. Each student should have a name, department, marks, and attendance. Write functions to: (1) calculate the average marks, (2) find the student with the highest marks, and (3) count students with attendance below 80%. Use for loops inside your functions. Finally, print a short summary of the results."""


student_list = [
    {"name": "Naruto", "department": "CSE", "marks": 75, "attendance": 90},
    {"name": "Sasuke", "department": "Data Science", "marks": 97, "attendance": 98},
    {"name": "Eren", "department": "CSE", "marks": 92, "attendance": 95},
    {"name": "Bakugo", "department": "EEE", "marks": 98, "attendance": 100},
    {"name": "Izuku", "department": "Data Science", "marks": 88, "attendance": 90}
]



def calculate_average(students):
    total = 0

    for student in students:
        total = total + student["marks"]

    average = total / len(students)
    return average

print("avergage: ", calculate_average(student_list))

def highest_marks(students):
    highest = students[0]

    for student in students:
        if student["marks"] > highest["marks"]:
            highest = student

    return highest
top_student = highest_marks(student_list)
print("highest mark: ", top_student["marks"], " acheived by ", top_student["name"])

def count_low_attendance(students):
    count = 0

    for student in students:
        if student["attendance"] < 80:
            count = count + 1

    return count

print("low attanedence: ", count_low_attendance(student_list))