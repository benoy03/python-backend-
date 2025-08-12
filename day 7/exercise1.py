class Person:
    """A class to represent a person with a name and age."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        """Returns an introductory string for the person."""
        return f"Hello, my name is {self.name} and I am {self.age} years old."


print("--- Exercise 1: Person Class with User Input ---")
try:
    name1 = input("Enter the name for the first person: ")
    age1 = int(input("Enter the age for the first person: "))
    person1 = Person(name1, age1)

    name2 = input("Enter the name for the second person: ")
    age2 = int(input("Enter the age for the second person: "))
    person2 = Person(name2, age2)

    print("\nIntroduction from first person:")
    print(person1.introduce())
    print("\nIntroduction from second person:")
    print(person2.introduce())
except ValueError:
    print("Invalid age. Please enter a number.")
print("-" * 25)