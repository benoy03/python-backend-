class Person:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.__email = email

    def display_info(self):
        print(f"ID: {self.id}, Name: {self.name}, Email: {self.__email}")

    def get_email(self):
        return self.__email

    def __repr__(self):
        return f"Person({self.id!r}, {self.name!r}, {self.__email!r})"


class Student(Person):
    def __init__(self, id, name, email, major, gpa):
        super().__init__(id, name, email)
        self.major = major
        self.gpa = gpa
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def __lt__(self, other):
        return self.gpa < other.gpa

    def __repr__(self):
        return f"Student({self.id!r}, {self.name!r}, GPA={self.gpa!r})"


class Professor(Person):
    def __init__(self, id, name, email, department):
        super().__init__(id, name, email)
        self.department = department
        self.courses_teaching = []

    def add_course(self, course):
        self.courses_teaching.append(course)
#__lt__ → < compares GPAs between students.
#repr__ → debug-friendly string showing object details.