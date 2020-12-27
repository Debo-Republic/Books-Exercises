# Working with Classes.
# Writing methods inside that uses the attributes.

class Car:
    """ A class that models a real life car in a oversimplified way."""

    def __init__(self, make, model, year):
        """Function to store key attributes of the car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def describe_car(self):
        """Function to print the name of the car in a clear fashion."""
        car_description = f"{self.year} {self.make} {self.model}"
        return car_description.title()

    def read_odometer(self):
        """Function to print the car's mileage"""
        print(f"The {self.model} has {self.odometer} miles on it.")

    def update_odometer(self, value):
        """Function to update the value of odometer and avoid rollback."""
        if value >= self.odometer:
            self.odometer = value
        else:
            print("odometer can't be rolled back!")

    def increment_odometer(self, miles):
        """Function to increment odometer for every road trip."""
        self.odometer += miles


my_new_car = Car('Lambhorghini', 'aventedor', 2014)

# Calling my_new_car.describe_car() method returns a value which needs printing
print(my_new_car.describe_car())
# Calling read_odometer() prints the mileage directly
my_new_car.read_odometer()

# Modifying the value of the attribute directly
my_new_car.odometer = 23
my_new_car.read_odometer()

# Updating attributes through methods
my_new_car.update_odometer(53)
my_new_car.read_odometer()

# Updating attributes directly through methods
my_new_car.update_odometer(20)
my_new_car.read_odometer()

# Operating before updating the methods
my_new_car.increment_odometer(30)
my_new_car.read_odometer()