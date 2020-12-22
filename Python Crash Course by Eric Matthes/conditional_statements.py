#understanding if statements 
moisturizers = ['cosrx', 'klairs', 'sunday', 'yttp']
for cream in moisturizers:
	if cream == 'cosrx' :
		print(f"the only good cream is {cream}")
	else :
		print(f"{cream} sucks")

#Conditional tests on equality 
finals = ['mi', 'ams', 'ml']
today = 'ams'

if today == 'ams':
	print(f"today was {today} finals. Probably going to ace it.")

#Conditional test on checking for inequality 
if today != 'ams':
	print("not equal to anything.")
else:
	print(f"How did your {today} paper go ?")

# and, or and membership functions 
#Some important folks hate musrooms so had to put this in the file 

toppings = ['peperoni', 'mushrooms', 'chicken']
print('mushrooms' in toppings)