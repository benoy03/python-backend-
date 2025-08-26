import sqlite3
from tabulate import tabulate


conn = sqlite3.connect("student_db.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
""")
conn.commit()

def add_student(name, age, grade):
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", 
                   (name, age, grade))
    conn.commit()
    print(f"Student {name} added successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    if rows:
        print(tabulate(rows, headers=["ID", "Name", "Age", "Grade"], tablefmt="grid"))
    else:
        print("No students found.")

def update_student(student_id, new_grade):
    cursor.execute("UPDATE students SET grade = ? WHERE id = ?", 
                   (new_grade, student_id))
    conn.commit()
    print(f"Student {student_id} updated successfully!")

def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print(f"Student {student_id} deleted successfully!")

if __name__ == "__main__":
    add_student("John", 21, "B")
    add_student("Sara", 19, "A")
    view_students()
    
    update_student(1, "A+")
    view_students()
    
    delete_student(2)
    view_students()
