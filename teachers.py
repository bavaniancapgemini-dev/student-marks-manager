def add_teacher():

    name = input(
        "Teacher Name: "
    )

    subject = input(
        "Subject: "
    )

    file = open(
        "teachers.txt",
        "a"
    )

    file.write(
        name + "," + subject + "\n"
    )

    file.close()

    print(
        "Teacher Added"
    )

def view_teachers():

    file = open(
        "teachers.txt",
        "r"
    )

    print()

    print("TEACHERS")

    for line in file:

        print(
            line.strip()
        )

    file.close()