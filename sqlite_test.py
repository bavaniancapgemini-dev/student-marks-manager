import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    name TEXT,
    marks INTEGER
)
""")

connection.commit()

connection.close()

print("Table Created")