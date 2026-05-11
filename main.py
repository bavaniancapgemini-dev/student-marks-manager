from grades import calculate_grade
students = {}
marks = int(input("Enter marks: "))

grade = calculate_grade(marks)

print("Grade:", grade)

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Student name: ")
        marks = input("Marks: ")
        students[name] = marks
        print("Student added!")

    elif choice == "2":
        print("\nStudent Records:")
        for name, marks in students.items():
            print(name, ":", marks)

    elif choice == "3":
        break

    else:
        print("Invalid choice")