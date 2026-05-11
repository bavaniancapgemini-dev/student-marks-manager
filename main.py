from grades import calculate_grade
from database import save_student
from utils import title
from report import show_report, topper
from database import delete_student
from database import update_student
from report import search_student
from report import average_marks
students = {}
name = input("Enter student name: ")
marks = int(input("Enter marks: "))

save_student(name, marks)
grade = calculate_grade(marks)

print("Grade:", grade)

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Show Report")
    print("4. Delete Student")
    print("6. Update Marks")
    print("7. Search student")
    print("8. Average Marks")
    print("9. show Topper")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Student name: ")
        marks = input("Marks: ")
        students[name] = marks
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

    elif choice == "5":
        break

    else:
        print("Invalid choice")