# Exercise 9.6

class Restaurant:
    """A class that models basic information about a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialise restaurant name and overarching theme of cuisines."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 10

    def describe_restaurant(self):
        """Function to print restaurant name and cuisines housed."""
        print(f"{self.restaurant_name} is a {self.cuisine_type} theme restaurant.")

    def open_restaurant(self):
        """Function to print that the restaurant is open."""
        print(f"{self.restaurant_name} is open! Please keep masks on while eating!")


class IceCreamStand(Restaurant):
    """A ice cream stand that has restaurant inherited properties."""

    def __init__(self, restaurant_name, cuisine_type, flavours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours

    def desc_flavours(self):
        print(f"The flavours available are {self.flavours}")


vadilal = IceCreamStand('vadilaal', 'Ice Cream', 'Orange and vanilla')
vadilal.desc_flavours()