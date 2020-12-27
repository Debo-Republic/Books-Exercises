# Division of real models into smaller attributes.

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
        self.battery = Battery()

    def fill_gas_tank(self):
        """Method to override the gas tank."""
        print("Electric cars don't have a glass tank.")


# Battery as a seperate class to be used as attributes.
class Battery():
    """
    A class to represent the battery units of car.
    To be used as attribute parent class.
    """
    def __init__(self, battery_size=75):
        """Initialise the battery's attributes."""
        self.battery_size = battery_size

    def desc_battery_size(self):
        """A function to print the size of battery in the class."""
        print(f"The battery size of the car is {self.battery_size}")

    def get_range(self):
        """Function to print the range of the vehicle from battery size."""
        if self.battery_size <= 75:
            range = 260
        elif self.battery_size >= 100:
            range = 300
        
        print(f"The range for {self.battery_size} kWh battery is {range}.")


my_tesla = Electric('tesla', 'model s', '2020')
# Changing the attribute value from the default 75 to 100.
my_tesla.battery.battery_size = 100
# Printing the attribute value by calling the class.
my_tesla.battery.desc_battery_size()
my_tesla.battery.get_range()