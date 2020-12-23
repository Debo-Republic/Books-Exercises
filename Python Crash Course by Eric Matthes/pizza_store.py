#Pizza store 
available_toppings = ['Pepperoni', 'cheese', 'jalapenos', 'chicken', 'pineapple']
requested_toppings = ['greeen_apple', 'chicken' , 'Pepperoni']

if requested_toppings:
	for items in requested_toppings:
		if items in available_toppings:
			print(f"Adding {items} to your pizza")
		else:
			print(f"Sorry {items} is currently not available. ")
			print(f"The available toppings are {available_toppings}")


else:
	print("Ordering a plain pizza for you. How boring!")