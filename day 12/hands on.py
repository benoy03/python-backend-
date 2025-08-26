import sqlite3


conn = sqlite3.connect("school.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
""")


cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", 
               ("Alice", 20, "A"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", 
               ("Bob", 22, "B"))


cursor.execute("SELECT * FROM students")
print("Students:", cursor.fetchall())

cursor.execute("UPDATE students SET grade = ? WHERE name = ?", ("A+", "Bob"))


cursor.execute("DELETE FROM students WHERE name = ?", ("Alice",))


conn.commit()
conn.close()
