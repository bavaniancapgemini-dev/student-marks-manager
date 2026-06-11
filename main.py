from analytics import *
from export import *
from ranking import *
from attendance import *
from subjects import *
from dashboard import *
from grades import calculate_grade
from database import save_student
from utils import title
from report import show_report, topper
from database import delete_student
from database import update_student
from report import search_student
from report import average_marks
from teachers import *
from fees import *
from classes import *
from school_dashboard import *
from exams import *
from timetable import *
from parents import *
from login import *
from analytics_v2 import *
from report_card import *
from admin import *
from teacher_login import *
from salary import *
from library import *
from inventory import *
from kpi import *

students = {}
while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Show Report")
    print("4. Delete Student")
    print("6. Update Marks")
    print("7. Search student")
    print("8. Average Marks")
    print("9. show Topper")
    print("10. Filed Students")
    print("11. Grade Statistics")
    print("12. Student Ranking")
    print("13. Export Report")
    print("14. Mark Attendance")
    print("15. View Attendance")
    print("16. Add Subject Marks")
    print("17. Calculate Percentage")
    print("18. Student Dashboard")
    print("19. Pass/Fail Report")
    print("20. Add Teacher")
    print("21. View Teachers")
    print("22. Pay Fees")
    print("23. Fee Report")
    print("24. Fee Defaulters")
    print("25. Assign Class")
    print("26. School Dashboard")
    print("27. Schedule Exams")
    print("28. View Exams")
    print("29. Add Timetable")
    print("30. View Timetable")
    print("31. Add Parent Record")
    print("32. Student Login")
    print("33. School Analytics")
    print("34. Generate Report Card")
    print("35. Admin Login")
    print("36. Teacher Login")
    print("37. Add Salary")
    print("38. Salary Report")
    print("39. Add Book")
    print("40. View Books")
    print("41. Issue Book")
    print("42. Add Inventory")
    print("43. View Inventory")
    print("44. KPI Dashboard")
    print("45. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Student name: ")
        marks = input("Marks: ")
        students[name] = marks
        save_student(name,int(marks))

        grade = calculate_grade(int(marks))

        print("Grade:", grade)
        print("Student added!")

    elif choice == "2":
        title("STUDENT RECORDS")
        for name, marks in students.items():
            print(name, ":", marks)

    elif choice == "3":
        show_report()

    elif choice == "4":

        name = input("Enter student name to delete: ")

        delete_student(name)

        print("Student Deleted")

    elif choice == "6":

        name = input("Enter student name: ")

        new_marks = int(input("Enter new marks: "))

        update_student(name, new_marks)

        print("Marks Updated")

    elif choice == "7":

        name = input("Enter student name: ")

        search_student(name)

    elif choice == "8":

        average_marks()

    elif choice == "9":

        topper()

    elif choice == "10":
        failed_students()

    elif choice == "11":
        grade_statistics()

    elif choice == "12":
        student_ranking()

    elif choice == "13":
        export_report()

    elif choice == "14":
        mark_attendance()

    elif choice == "15":
        view_attendance()

    elif choice == "16":
        add_subject_marks()

    elif choice == "17":
        calculate_percentage()

    elif choice == "18":
        student_dashboard()

    elif choice == "19":
        pass_fail_report()

    elif choice == "20":
        add_teacher()

    elif choice == "21":
        view_teachers()

    elif choice == "22":
        pay_fee()

    elif choice == "23":
        fee_report()
    
    elif choice == "24":
        fee_defaulters()

    elif choice == "25":
        assign_class()

    elif choice == "26":
        school_dashboard()

    elif choice == "27":
        schedule_exam()

    elif choice == "28":
        view_exams()

    elif choice == "29":
        add_timetable()

    elif choice == "30":
        view_timetable()

    elif choice == "31":
        add_parent()

    elif choice == "32":
        student_login()

    elif choice == "33":
        school_analytics()

    elif choice == "34":
        generate_report_card()

    elif choice == "35":
        admin_login()

    elif choice == "36":
        teacher_login()

    elif choice == "37":
        add_salary()

    elif choice == "38":
        salary_report()

    elif choice == "39":
        add_book()

    elif choice == "40":
        view_books()

    elif choice == "41":
        issue_book()

    elif choice == "42":
        add_inventory()

    elif choice == "43":
        view_inventory()

    elif choice == "44":
        kpi_dashboard()

    elif choice == "45":
        break

    else:
        print("Invalid choice")