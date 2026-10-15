# ----- LAB CLASS 2 - EXERCISE 1 ---

""" Create variables to store a student's name, student ID, department, and grade. Store the student's name, student ID, and department as strings. Store the grade as a number. Print a simple student profile using a clear format."""

print(" STUDENT INFORMARION\n ")
student_info = {
    "student_name": "ipshita",
    "student_id": "25-61638-1",
    "dept" : "data science",
    "grade" : 88.0
    }
student_name = "ipshita"
student_id = "25-61638-1"
dept = "data science"
grade = 88.0

print(f"students name is {student_name}, students id is {student_id}, students department is {dept}, students grade is {grade}")

print(" STUDENT INFORMARION\n ")

student_name = input("Enter student's name: ")
student_id = input("Enter student's ID: ")
dept = input("Enter department name: ")
cgpa = float(input("Enter student's cgpa: "))
print(f"students name is {student_name}, id is {student_id}, he is from {dept} department and students grade is {cgpa}")