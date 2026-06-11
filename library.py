def add_book():

    book = input(
        "Book Name: "
    )

    file = open(
        "library.txt",
        "a"
    )

    file.write(
        book + "\n"
    )

    file.close()

    print(
        "Book Added"
    )

def view_books():

    file = open(
        "library.txt",
        "r"
    )

    print()

    print("LIBRARY BOOKS")

    for line in file:

        print(
            line.strip()
        )

    file.close()

def issue_book():

    student = input(
        "Student Name: "
    )

    book = input(
        "Book Name: "
    )

    file = open(
        "issued_books.txt",
        "a"
    )

    file.write(
        student + "," +
        book + "\n"
    )

    file.close()

    print(
        "Book Issued"
    )