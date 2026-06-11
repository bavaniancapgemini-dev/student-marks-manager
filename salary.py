def add_salary():

    teacher = input(
        "Teacher Name: "
    )

    salary = int(
        input("Salary: ")
    )

    file = open(
        "salary.txt",
        "a"
    )

    file.write(
        teacher + "," +
        str(salary) + "\n"
    )

    file.close()

    print(
        "Salary Recorded"
    )

def salary_report():

    total = 0

    file = open(
        "salary.txt",
        "r"
    )

    for line in file:

        total += int(
            line.strip().split(",")[1]
        )

    file.close()

    print()

    print(
        "Total Salary Expense:",
        total
    )