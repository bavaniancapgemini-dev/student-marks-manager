import sqlite3

conn = sqlite3.connect(
    "school.db"
)

cursor = conn.cursor()

cursor.execute(
"""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
marks INTEGER
)
"""
)

conn.commit()

def add_student_db(
    name,
    marks
):

    conn = sqlite3.connect(
        "school.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO students(
        name,
        marks
        )
        VALUES(?,?)
        """,
        (
            name,
            marks
        )
    )

    conn.commit()

    conn.close()

def view_students_db():

    conn = sqlite3.connect(
        "school.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students"
    )

    data = cursor.fetchall()

    conn.close()

    return data

def search_student_db():

    student_id = int(
        input(
            "Student ID: "
        )
    )

    conn = sqlite3.connect(
        "school.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM students
        WHERE id = ?
        """,
        (student_id,)
    )

    print(
        cursor.fetchone()
    )

    conn.close()

def delete_student_db():

    student_id = int(
        input(
            "Student ID: "
        )
    )

    conn = sqlite3.connect(
        "school.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM students
        WHERE id = ?
        """,
        (student_id,)
    )

    conn.commit()

    conn.close()

    print(
        "Deleted"
    )