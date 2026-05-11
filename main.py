from grades import calculate_grade
from database import save_student
from utils import title
from report import show_report
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
    print("4. Exit")

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
        break
    
    else:
        print("Invalid choice")