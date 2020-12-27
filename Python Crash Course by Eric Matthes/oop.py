# Using classes to model a dog.
# Each dog will have a name, age, ability to sit and rollover.

class Dog:
    """Modelling a dog with basic information and behaviours."""
    def __init__(self, name, age):
        """ Initialise name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} is now rolled over.")


# Making instances of the class & calling attributes.
my_dog = Dog('Don', 14)
print(f"My Dog's name is {my_dog.name}")
print(f"My Dog {my_dog.name} is {my_dog.age} years old. ")

# Calling the methods defined in the class.
my_dog.sit()
my_dog.roll_over()