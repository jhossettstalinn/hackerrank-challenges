from collections import namedtuple

total_number_students = int(input())

if total_number_students <= 0 or total_number_students > 100:
    print("Enter a number between 1 and 100")
    exit()

students = namedtuple('students', input().split())

sum_marks = 0
for _ in range(total_number_students):
    student_info = students(*input().split())
    sum_marks += float(student_info.MARKS)
print(f"{sum_marks/total_number_students:.2f}")