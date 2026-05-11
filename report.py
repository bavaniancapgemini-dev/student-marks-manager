def show_report():

    file = open("students.txt", "r")

    data = file.readlines()

    file.close()

    print("\n---- REPORT ----")

    for line in data:
        print(line.strip())