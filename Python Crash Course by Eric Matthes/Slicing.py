#A few ways to slice a list 
fall_subjects = ['SMD', 'WSC', 'AMS', 'MI','ML','DLD']
print(fall_subjects[:])
print(fall_subjects[2:])

for sub in fall_subjects[0:3]:
	print(sub)

neigbhorhoods = ['uws', 'ues', 'downtown', 'nyu']
for places in neigbhorhoods[1:]:
	print(f" The only good places to visit in NY is {places}")

#SLicing and Copying: 
my_food = ['Chicken Breast', 'Brocoli', 'Salt']
her_food = my_food[0:2]
print(my_food)
print(her_food)
her_food.append('ice cream')
print(her_food)

#Concept of shallow copy 
my_food = her_food
print(my_food)
print(her_food)
my_food.append('beef')
#Since both pointers point towards the same direction
print(her_food)
#contingency = Deep copy using slicing  
their_food = her_food[:]
her_food.append('cheescake')
print(their_food)

#exercise 4-10
print(f"The first three items of her food  are {her_food[0:3]}")
print(f"The middle three items of her food are {her_food[1:4]}")
print(f"The last three items of her food are {her_food[2:]}")

#Making seperate copy of lists 
my_pizza = ['cheese', 'margherita','Chicken']
her_pizza = my_pizza[:]
my_pizza.append('Pepperoni')
her_pizza.append('farmhouse')
for pizza in her_pizza:
	print(f"The the pizzas she likes are {pizza}")

for pizza in my_pizza:
	print(f"The pizzas I like are {pizza}")