def add_parent():

    student = input(
        "Student Name: "
    )

    parent = input(
        "Parent Name: "
    )

    phone = input(
        "Phone Number: "
    )

    file = open(
        "parents.txt",
        "a"
    )

    file.write(
        student + "," +
        parent + "," +
        phone + "\n"
    )

    file.close()

    print(
        "Parent Added"
    )