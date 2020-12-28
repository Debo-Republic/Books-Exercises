# Program to find users favorite number.
# Import all required libraries.
import json

def fav_num():
    """Function to store users favourite number."""
    user_name = input("Give me your name!")
    fav_number = input("Give me your number! Favourite number, I mean.")
    message = f"{user_name}'s favourite number is {fav_number}"
    print(message)
    return message

def save_data(message,filename):
    """Function to save the user data."""
    with open(filename, 'a') as f:
        json.dump(message, f)


filename = 'favourite_number.json'
message = fav_num()
save_data(message, filename)

