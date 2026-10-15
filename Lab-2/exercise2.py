#  LAB-2 EXERCISE 2

marks = []
for i in range(1, 6):
    mark = float(input(f"Enter mark for course {i}: "))
    marks.append(mark)

def grade_calculator(grade):
    total_grade = sum(grade)
    average = total_grade/ len(marks)
    highest_grade = max(marks)
    lowest_grade = min(marks)

    passed_courses = 0
    for mark in marks:
        if mark >= 50:
            passed_courses += 1

    print(f"total grade: {total_grade}")
    print(f"the average score: {average}")
    print(f"highest grade: {highest_grade}")
    print(f"lowest grade: {lowest_grade}")
    print(f"number of passed courses {passed_courses}")
    
grade_calculator(marks)


data_processing = float(input("Enter your data processing grade: "))
pds = float(input("Enter your data pds: "))
data_science = float(input("Enter your data science grade: "))
python = float(input("Enter your python grade: "))

course_marks = [data_processing, pds, data_science, python]
def grade_calculator(grade):
    total_grade = sum(grade)
    average = total_grade/ len(course_marks)
    highest_grade = max(course_marks)
    lowest_grade = min(course_marks)

    passed_courses = 0
    for mark in course_marks:
        if mark >= 50:
            passed_courses += 1

    print(f"total grade: {total_grade}")
    print(f"the average score: {average}")
    print(f"highest grade: {highest_grade}")
    print(f"lowest grade: {lowest_grade}")
    print(f"number of passed courses {passed_courses}")
grade_calculator(course_marks)