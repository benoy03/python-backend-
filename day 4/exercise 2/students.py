students = []
adding_students = True  

print("=== Student Info Collection ===")

while adding_students:
    name = input("Student Name: ")
    age = input("Student Age: ")
    major = input("Student Major: ")

    student = (name, age, major)
    students.append(student)

    choice = input("Do you want to add another student? (y/n): ").strip().lower()
    if choice != 'y':
        adding_students = False

print("\n=== All Students Entered ===")
for i, student in enumerate(students, start=1):
    print(f"{i}. Name: {student[0]}, Age: {student[1]}, Major: {student[2]}")
