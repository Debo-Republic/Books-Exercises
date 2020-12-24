dog = { 
	'name' : 'Don',
	'owner' : 'Promod', 
	'nature' : 'unpredictable',
	'gender' : 'Male',
	'breed' : 'Dalmatian',
}

cat = {
	'name' : 'iris', 
	'owner' : 'Jean',
	'nature' : 'Soft',
	'gender' : 'Female' ,
	'breed' : 'Ragdoll',
}

pets = [cat, dog]

for pet in pets:
	print(f" \n the {pet} has the following information listed")
	for k,v in pet.items():
		print(f"{k} is {v}")

# how to print the name of the dictionary ?