# Defining a restaurant using object oriented programming.

class Restaurant:
    """A class that models basic information about a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialise restaurant name and overarching theme of cuisines."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Function to print restaurant name and cuisines housed."""
        print(f"{self.restaurant_name} is a {self.cuisine_type} theme restaurant.")

    def open_restaurant(self):
        """Function to print that the restaurant is open."""
        print(f"{self.restaurant_name} is open! Please keep masks on while eating!")


# Defining a User class that stores multiple information about user.

class User:
    """A Class that stores information about the users."""

    def __init__(self, user_name, user_age, user_gender):
        """Method to store ket attributes of user."""
        self.user_name = user_name
        self.user_age = user_age
        self.user_gender = user_gender

    def describe_user(self):
        """A method to describe information about users."""
        print(f"The name of user is {self.user_name}")
        print(f" User is {self.user_age} years old.")
        print(f"User is {self.user_gender}")

    def greet_user(self):
        """Function to greet user with a message."""
        print(f"Hi {self.user_name}! You look terrible today! ")


# Instantiating a restaurant.
toit = Restaurant('TOIT', 'Micro Brewery')
toit.describe_restaurant()
toit.open_restaurant()

# Instantiating a user.
user_1 = User('AYOTA', '92', 'Male')
user_1.describe_user()
user_1.greet_user()
