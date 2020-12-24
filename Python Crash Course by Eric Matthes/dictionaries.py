#key value pair
#definition
aliens = {'colors' : 'greens', 'points' : 5}

#access by keys 
print(f"if you manage to shoot {aliens['colors']} coloured alins then you will get ")
print(f"{aliens['points']} points")

aliens['x_position'] = 0
aliens['y_position'] = 25
print(aliens)

#empty dictionaries are initialised like any other empty data structure 
kushal = {}
print(kushal)

#modifying the value stored in a key value pair

print(f"initially the alien's color was {aliens['colors']}")
aliens['colors'] = 'blue'
print(f"now i have changed the alien's color to {aliens['colors']}")

#Giving them aliens some speed : 
#lets assume there are three types of speed availabe 
#slow, fast & medium 

aliens['speed'] = 'slow'

#define what speed is only interms of incremnet: 
if aliens['speed'] == 'slow' :
	x_increment = 1
elif aliens['speed']== 'medium' :
	x_increment = 2
elif aliens['speed'] == 'fast' :
	x_increment = 3

#increment the position of x once interms of its speed 
aliens['x_position'] = aliens['x_position'] + x_increment

print(f"the new positon of alien is {aliens['x_position']}")

#removing key value pairs from the dictionariesby deleting keys 
del aliens['points']
print(aliens)

#writing long dictionaries beautifully : 

#favourite programming languages of friends : 

programming_languages = {
	'debo' : 'any language will do',
	'mayu' : 'salesforce',
	'jaison' : 'html',
	'bose' : 'R',

}
print(programming_languages)

#using get method to access the key value pair instead of []. 
#defaulting to a message if a key value pair isn't found.


print(programming_languages.get('points', 'This freaking key no existoo!'))