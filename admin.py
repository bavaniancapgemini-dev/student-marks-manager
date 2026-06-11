def admin_login():

    username = input(
        "Admin Username: "
    )

    password = input(
        "Admin Password: "
    )

    if (
        username == "admin"
        and
        password == "admin123"
    ):

        print(
            "Admin Login Successful"
        )

    else:

        print(
            "Invalid Admin Login"
        )