from database import view_students

def kpi_dashboard():

    students = view_students()

    print()

    print("SCHOOL KPI DASHBOARD")

    print("--------------------")

    print(
        "Total Students:",
        len(students)
    )