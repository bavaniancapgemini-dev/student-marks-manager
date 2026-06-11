def pay_fee():

    student = input(
        "Student Name: "
    )

    amount = int(
        input("Fee Amount: ")
    )

    file = open(
        "fees.txt",
        "a"
    )

    file.write(
        student + "," +
        str(amount) + "\n"
    )

    file.close()

    print(
        "Fee Recorded"
    )

def fee_report():

    file = open(
        "fees.txt",
        "r"
    )

    total = 0

    for line in file:

        amount = int(
            line.strip().split(",")[1]
        )

        total += amount

    print()

    print(
        "Total Fees Collected:",
        total
    )

    file.close()

def fee_defaulters():

    students = []

    file = open(
        "students.txt",
        "r"
    )

    for line in file:

        students.append(
            line.split(",")[0]
        )

    file.close()

    paid = []

    try:

        file = open(
            "fees.txt",
            "r"
        )

        for line in file:

            paid.append(
                line.split(",")[0]
            )

        file.close()

    except:

        pass

    print()

    print("FEE DEFAULTERS")

    for student in students:

        if student not in paid:

            print(student)