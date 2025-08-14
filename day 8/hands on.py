class Vehicle:
    def move(self):
        print("The vehicle moves.")

class Car(Vehicle):
    def move(self):
        print("The car drives on roads.")

class Boat(Vehicle):
    def move(self):
        print("The boat sails on water.")

print("Choose a vehicle type:")
print("1. Car")
print("2. Boat")
choice = input("Enter choice (1 or 2): ")

if choice == "1":
    vehicle = Car()
elif choice == "2":
    vehicle = Boat()
else:
    print("Invalid choice.")
    exit()


vehicle.move()
