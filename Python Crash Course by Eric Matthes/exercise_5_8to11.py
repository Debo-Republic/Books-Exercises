#Hello lonely admin:
usernames = ['admin', 'debo', 'mayu', 'niko', 'chicko']
for folks in usernames:
	if folks == 'admin':
		print("Hello admin, would you like to see and status report ?")
	else:
		print(f"Hello {folks}, thank you for logging in again.")


#case of no users:
logged_in = []
if logged_in :
	print("we gotta find some goddamn users !")
else :
	print("Thank god some users finally.")

current_users = ['cem' , 'janice', 'ella', 'saisha' , 'debo']
new_users = ['cem' , 'robert', 'kamel']

for items in new_users:
	if items.lower() in [name.lower() for name in current_users ]:
		print("The username already exists and is not available!")
	else : 
		print(f"{items} is good to go!")