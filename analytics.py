from database import view_students

def failed_students():

    students = view_students()

    print()

    print("FAILED STUDENTS")

    for student in students:

        if student[1] < 35:

            print(
                student[0],
                "-",
                student[1]
            )
        
from grades import calculate_grade

def grade_statistics():

    students = view_students()

    grades = {}

    for student in students:

        grade = calculate_grade(
            student[1]
        )

        grades[grade] = (
            grades.get(grade, 0) + 1
        )

    print()

    print("GRADE STATISTICS")

    for grade, count in grades.items():

        print(
            grade,
            ":",
            count
        )