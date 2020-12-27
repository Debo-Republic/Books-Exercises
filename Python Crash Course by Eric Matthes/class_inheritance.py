# Examples to see class inheritance

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

    def fill_gas_tank(self):
        """Function to simulate filling glass tanks."""
        print("Thanks for filling the gas!")


# Working with an inherited class.
class Electric(Car):
    """Special child class of regular cars. """

    def __init__(self, make, model, year):
        """All attributes inherited from parent class."""
        super().__init__(make, model, year)
        self.battery_size = 100

    def describe_battery(self):
        """Method to print the battery size of the electric vehicle."""
        print(f"The battery size of the vehicle is {self.battery_size} kWh.")

    def fill_gas_tank(self):
        """Method to override the gas tank."""
        print("Electric cars don't have a glass tank.")

# Working with an instance of inherited class.
my_tesla = Electric('tesla', 'model s', 2019)
print(my_tesla.describe_car())
my_tesla.describe_battery()
