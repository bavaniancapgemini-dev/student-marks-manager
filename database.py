def save_student(name, marks):

    file = open("students.txt", "a")

    file.write(name + "," + str(marks) + "\n")

    file.close()