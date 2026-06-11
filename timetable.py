def add_timetable():

    day = input(
        "Day: "
    )

    subject = input(
        "Subject: "
    )

    file = open(
        "timetable.txt",
        "a"
    )

    file.write(
        day + "," + subject + "\n"
    )

    file.close()

    print(
        "Timetable Updated"
    )

def view_timetable():

    file = open(
        "timetable.txt",
        "r"
    )

    print()

    print("TIMETABLE")

    for line in file:

        print(
            line.strip()
        )

    file.close()