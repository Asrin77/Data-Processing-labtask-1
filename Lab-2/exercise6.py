"""EXERCISE 6"""
"""06 • Grade Calculator Function

Write a function called calculate_grade(marks) that receives a list of marks. The function should calculate the average and return a grade using these rules: A for average ≥ 80, B for ≥ 70, C for ≥ 60, D for ≥ 50, and F for below 50. Call the function using a list of 5 marks."""

def calculate_grade(marks):
    avg = sum(marks)/len(marks)

    if avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"
mark_list = []
for i in range(0, 5):
    mark = float(input(f"enter mark {i+1}: "))
    mark_list.append(mark)

print(calculate_grade(mark_list))