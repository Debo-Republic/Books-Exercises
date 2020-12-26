# Arbitrary number of arguments to functions.
# Pizza toppings.
def make_pizza(size=8, *toppings):
    """Function to print the pizza toppings selected."""
    print(f"\n Making an {size} inch pizza with")
    for topping in toppings:
        print(f"\n {topping}")


make_pizza(10, 'Chicken')
make_pizza(2, 'cheese', 'chicken', 'pineapple')


# Keyword arguments
def user_info(
        first_name,
        last_name,
        **profile):
    """Function that builds user information."""
    profile['firstname'] = first_name
    profile['lastname'] = last_name
    return profile


user_profile = user_info('debopriyo', 'bhowmick', school="CBS", city='NYC')
print(user_profile)
