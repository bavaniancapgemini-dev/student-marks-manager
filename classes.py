def assign_class():

    name = input(
        "Student Name: "
    )

    class_name = input(
        "Class: "
    )

    file = open(
        "classes.txt",
        "a"
    )

    file.write(
        name + "," +
        class_name + "\n"
    )

    file.close()

    print(
        "Class Assigned"
    )