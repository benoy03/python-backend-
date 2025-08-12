class Dog:
    """A class to represent a dog with instance and class variables."""
   
    species = "Canis familiaris"

    def __init__(self, name, breed):
   
        self.name = name
        self.breed = breed

    def describe(self):
        """Returns a description of the dog."""
  
        return f"{self.name} is a {self.breed}. Species: {self.species}."


print("\n--- Exercise 2: Dog Class with User Input ---")
dog1_name = input("Enter the name for the first dog: ")
dog1_breed = input("Enter the breed for the first dog: ")
dog1 = Dog(dog1_name, dog1_breed)

dog2_name = input("Enter the name for the second dog: ")
dog2_breed = input("Enter the breed for the second dog: ")
dog2 = Dog(dog2_name, dog2_breed)

print(f"\nDog 1: {dog1.describe()}")
print(f"Dog 2: {dog2.describe()}")


dog1.species = "Canis lupus"  
print(f"\nAfter changing species for {dog1.name}:")
print(f"Dog 1: {dog1.describe()}")
print(f"Dog 2: {dog2.describe()}") 
print("-" * 25)
