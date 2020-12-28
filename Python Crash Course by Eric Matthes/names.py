# A user input program to produce formatted name.

from name_function import get_formatted_name

print("Enter q to quit anytime.")
while True:
    firstname = input("Enter your firstname")
    if firstname == 'q':
        break
    lastname = input("Enter your lastname.")
    if lastname == 'q':
        break
    fullname = get_formatted_name(firstname, lastname)
    print(f"The neatly formatted full name is {fullname}")
    print(f"\n Lets try again!")