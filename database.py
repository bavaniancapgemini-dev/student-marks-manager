import json
def save_student(name, marks):

    file = open("students.txt", "a")

    file.write(name + "," + str(marks) + "\n")

    file.close()

def delete_student(name):

    file = open("students.txt", "r")

    students = file.readlines()

    file.close()

    file = open("students.txt", "w")

    for student in students:

        if not student.startswith(name + ","):
            file.write(student)

    file.close()

def update_student(name, new_marks):

    file = open("students.txt", "r")

    students = file.readlines()

    file.close()

    file = open("students.txt", "w")

    for student in students:

        student_name = student.split(",")[0]

        if student_name == name:
            file.write(name + "," + str(new_marks) + "\n")

        else:
            file.write(student)

    file.close()

def save_json(student_data):

    file = open("students.json", "w")

    json.dump(student_data, file, indent=4)

    file.close()

def view_students():

    students = []

    file = open(
        "students.txt",
        "r"
    )

    for line in file:

        parts = line.strip().split(",")

        students.append(
            (
                parts[0],
                int(parts[1])
            )
        )

    file.close()

    return students

def generate_student_id():

    import random

    return (
        "STU"
        + str(
            random.randint(
                1000,
                9999
            )
        )
    )