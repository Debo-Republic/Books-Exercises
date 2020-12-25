#tshirts
def make_shirt(size = 'L', message = " I love python!"):
    """Displays information about a shirt"""
    print(f" \n This size of the requested shirt is {size} ")
    print(f"The message to be printed on the front is : \n {message}")

make_shirt(size = 'M', message= "An antidote to chaos!")
make_shirt()

#Cities
def describe_city(city, country = "USA"):
    """This functions prints a city and its country"""
    print(f"{city} is in {country}")

describe_city('Delhi', 'India')
describe_city('oregon')
describe_city(city='khalisthan', country='USA')