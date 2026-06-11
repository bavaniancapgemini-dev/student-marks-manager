def teacher_login():

    username = input(
        "Teacher Username: "
    )

    password = input(
        "Teacher Password: "
    )

    if (
        username == "teacher"
        and
        password == "teacher123"
    ):

        print(
            "Teacher Login Successful"
        )

    else:

        print(
            "Invalid Login"
        )