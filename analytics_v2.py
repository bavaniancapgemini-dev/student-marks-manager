from database import view_students

def school_analytics():

    students = view_students()

    total = len(students)

    print()

    print("SCHOOL ANALYTICS")

    print("----------------")

    print(
        "Total Students:",
        total
    )