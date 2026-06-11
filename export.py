from database import view_students

def export_report():

    students = view_students()

    file = open(
        "student_report.txt",
        "w"
    )

    for student in students:

        file.write(
            str(student) + "\n"
        )

    file.close()

    print(
        "Report Exported"
    )