def process_student(student_data):
    name = student_data.get('name')
    grade = student_data.get('grade')
    return name, grade

def average_grade(_grades):
    total = sum(_grades)
    average = total / len(_grades)
    return average

students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob'}, {'name': 'Jack', 'grade': 72},
    {'name': 'Jane', 'grade': 75},
]

def collect_grades(_students):
    grades = []
    for student in _students:
        name, grade = process_student(student)
        if grade:
            grades.append(grade)
    return grades

grades = collect_grades(students)
print(average_grade(grades))
# TypeError: unsupported operand type(s) for +: 'int'
# and 'NoneType'