class Car:
    """A class with a class variable to count total instances created."""
    total_cars = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.total_cars += 1

    def display_car(self):
        """Returns a string with the car's make and model."""
        return f"Car: {self.make} {self.model}"

    @staticmethod
    def get_total_cars():
        """Returns the total number of Car instances created."""
        return Car.total_cars


print("\n--- Exercise 5: Car Counter with User Input ---")
while True:
    create_car = input("Create a new car? (yes/no): ").lower()
    if create_car == 'yes':
        make = input("Enter car make: ")
        model = input("Enter car model: ")
        new_car = Car(make, model)
        print(new_car.display_car())
    elif create_car == 'no':
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

print(f"\nTotal cars created: {Car.get_total_cars()}")
print("-" * 25)