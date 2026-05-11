def show_report():

    file = open("students.txt", "r")

    data = file.readlines()

    file.close()

    print("\n---- REPORT ----")

    for line in data:
        print(line.strip())

def search_student(name):

    file = open("students.txt", "r")

    students = file.readlines()

    file.close()

    found = False

    for student in students:

        if student.startswith(name + ","):

            print("\nStudent Found:")
            print(student)

            found = True

    if not found:
        print("Student Not Found")

def average_marks():

    file = open("students.txt", "r")

    students = file.readlines()

    file.close()

    total = 0

    count = 0

    for student in students:

        marks = int(student.strip().split(",")[1])

        total += marks

        count += 1

    if count > 0:
        print("Average Marks:", total / count)

    else:
        print("No Records")

def topper():

    file = open("students.txt", "r")

    students = file.readlines()

    file.close()

    highest = 0
    topper_name = ""

    for student in students:

        data = student.strip().split(",")

        name = data[0]
        marks = int(data[1])

        if marks > highest:

            highest = marks
            topper_name = name

    print("\nTopper:")
    print(topper_name, "-", highest)