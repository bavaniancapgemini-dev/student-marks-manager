def check_login(
    username,
    password
):

    if (
        username == "admin"
        and
        password == "admin123"
    ):

        return True

    return False