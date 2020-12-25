# City names.
from typing import Dict, Any


def city_country(city_name, country):
    """function to identify city and country"""
    return f"{city_name.title()}, {country.title()}"


new = city_country('delhi', 'india')
print(new)
new = city_country('calcutta', 'india')
print(new)
new = city_country('new york', 'united states of america')
print(new)


# Album function
def make_album(artist_name, album_title, songs=None):
    """This function describes a music album."""
    album[artist_name.title()] = album_title.title()
    if songs:
        album['songs'] = songs
    return album


album = {}
this = make_album('eminem', 'curtain calls')
print(this)
this = make_album('khurangbin', 'texas sun')
print(this)
this = make_album('beck', 'loser')
print(this)
this = make_album('armin van buren', 'A state of trance', songs=10)
print(this)

# accepting albums from user
while True:
    artist_name = input("Enter an artist of your choice.")
    album_name = input("Enter one the the artist's albums.")
    songs = input("Enter the number of songs in the alubm.")
    this = make_album(artist_name, album_name, songs)
    print("The following is the history of user's best artists : \n")
    print(this)
    flag = input("Would you like to continue ?(Yes/ No)")
    if flag == 'No':
        break


