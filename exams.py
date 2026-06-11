def schedule_exam():

    subject = input(
        "Subject: "
    )

    date = input(
        "Exam Date: "
    )

    file = open(
        "exams.txt",
        "a"
    )

    file.write(
        subject + "," + date + "\n"
    )

    file.close()

    print(
        "Exam Scheduled"
    )

def view_exams():

    file = open(
        "exams.txt",
        "r"
    )

    print()

    print("EXAM SCHEDULE")

    for line in file:

        print(
            line.strip()
        )

    file.close()