#person i know - Nikoleta someranomlastname 

friend = {
	'first_name' : 'Nikoleta',
	'last_name' : 'someranomlastname',
	'age' : 25,
	'city' : 'New York',
	'neighborhood' : 'upper_west_side',
}

print(friend)

#printing  all information using a for loop 
print('the above dictionary can be printed in a much better format.')

for k, v in friend.items():
	print(f"Key : {k}")
	print(f"Value : {v} \n")

#Looping all the keys in an implicit or explicit way ; 

#Implicit
for keys in friend:
	print(f" the keys of this dictionary are {keys}")

#Explicit 
for keysagain in friend.keys():
	print(f"printing the same set of keys again {keysagain}")


#Printing a value of only a ceraitng key 
for keyu in friend :
	print(f"The key is {keyu}")
	if friend.get(keyu) == 'upper_west_side':
		print("Well, nice to see the low key upper_west_side folks.")


#Looping through keys in a sorted order. 
for sorted_keys in sorted(friend):
	print(f"The sorted keys can be printed by {sorted_keys}")

#looping through all the values
