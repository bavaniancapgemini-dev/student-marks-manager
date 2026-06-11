from database import view_students

def student_ranking():

    students = view_students()

    students.sort(
        key=lambda x: x[1],
        reverse=True
    )

    rank = 1

    for student in students:

        print(
            rank,
            "-",
            student[0],
            "-",
            student[1]
        )

        rank += 1