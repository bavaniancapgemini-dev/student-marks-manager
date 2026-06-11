def add_subject_marks():

    name = input(
        "Student Name: "
    )

    maths = int(
        input("Maths: ")
    )

    science = int(
        input("Science: ")
    )

    english = int(
        input("English: ")
    )

    file = open(
        "subjects.txt",
        "a"
    )

    file.write(
        f"{name},{maths},{science},{english}\n"
    )

    file.close()

    print(
        "Subject Marks Saved"
    )

def calculate_percentage():

    name = input(
        "Student Name: "
    )

    file = open(
        "subjects.txt",
        "r"
    )

    for line in file:

        data = line.strip().split(",")

        if data[0] == name:

            total = (
                int(data[1])
                + int(data[2])
                + int(data[3])
            )

            percentage = total / 3

            print(
                "Percentage:",
                round(percentage,2)
            )

    file.close()