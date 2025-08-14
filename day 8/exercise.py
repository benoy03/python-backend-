import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


shapes = []

while True:
    print("\nChoose a shape to add:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Finish")
    choice = input("Enter choice: ")

    if choice == "1":
        r = float(input("Enter radius: "))
        shapes.append(Circle(r))
    elif choice == "2":
        w = float(input("Enter width: "))
        h = float(input("Enter height: "))
        shapes.append(Rectangle(w, h))
    elif choice == "3":
        break
    else:
        print("Invalid choice.")


print("\n--- Shapes Summary ---")
for shape in shapes:
    print(f"{shape.__class__.__name__}: Area = {shape.area():.2f}, Perimeter = {shape.perimeter():.2f}")
