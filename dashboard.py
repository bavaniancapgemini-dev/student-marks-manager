from database import view_students

def student_dashboard():

    students = view_students()

    print()

    print("STUDENT DASHBOARD")

    print("----------------")

    print(
        "Total Students:",
        len(students)
    )

def pass_fail_report():

    students = view_students()

    passed = 0
    failed = 0

    for student in students:

        if student[1] >= 35:

            passed += 1

        else:

            failed += 1

    print()

    print(
        "Passed:",
        passed
    )

    print(
        "Failed:",
        failed
    )