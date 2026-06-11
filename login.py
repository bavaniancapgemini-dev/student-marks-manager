def student_login():

    username = input(
        "Username: "
    )

    password = input(
        "Password: "
    )

    if (
        username == "student"
        and
        password == "1234"
    ):

        print(
            "Login Successful"
        )

    else:

        print(
            "Invalid Login"
        )