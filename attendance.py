def mark_attendance():

    name = input(
        "Student Name: "
    )

    status = input(
        "Present/Absent: "
    )

    file = open(
        "attendance.txt",
        "a"
    )

    file.write(
        name + "," + status + "\n"
    )

    file.close()

    print(
        "Attendance Saved"
    )

def view_attendance():

    file = open(
        "attendance.txt",
        "r"
    )

    print()

    print("ATTENDANCE REPORT")

    for line in file:

        print(
            line.strip()
        )

    file.close()