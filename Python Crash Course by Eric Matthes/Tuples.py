#Tuples as immuatble lists 
height = (5,11)
print(height)
#defining tuples of single elements
weight =(72,)
print(weight)

#Addition or subtractions isn't possible, but we can write over entire values of the tuples
height =(4,11)
print(height)

#If you have to modify a tuple, you have to modify an entire tuple 
buffet = ('Ghee Rice', 'Chicken Tikka Masala', 'Salad', 'Dal', 'Gulab Jamun')
for items in buffet:
	print(f"The food available for today's buffet are {items}")

#Change of  buuffet items because of Corona 
buffet = ('Ghee Rice', 'Chicken Tikka Masala', 'Salad', 'Dal', 'Vaccine')
for items in buffet:
	print(f"Sorry, our offerings have changed and we are only offering {items}")