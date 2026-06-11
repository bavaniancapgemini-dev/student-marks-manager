from database import view_students

def school_dashboard():

    students = view_students()

    print()

    print("SCHOOL DASHBOARD")

    print("----------------")

    print(
        "Total Students:",
        len(students)
    )