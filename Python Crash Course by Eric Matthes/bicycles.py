bicycles = ['trek', 'canondale', 'redline', 'specialised ']
print(bicycles)
#accessing elements and combining it with methods
print(bicycles[0].title())
print(bicycles[-1])
print(bicycles[-2].upper())

print(f"I inted to buy a {bicycles[0].title()} bycycle this summer")
#Printing names of friends from a simple list 
names = ['soumen goswami ', 'Jaison Justus', 'Shekhar Anand', 'Shrinjit Dash', 'Mayuri B Upadhaya']
print(f"One of my oldest & truest friend is {names[0].title()}")
print(f"an a typical friend who takes forever to respond {names[1].title()}")
print(f"A respectable friend, who sometimes ditches on me, but still a longstanding friend {names[2].title()}")
print(f"The only lifelong friend. Met her really late in my life : \t {names[-1].title()}")

dream_vehicle = ["Harley Davidson", "Aston Martin", "I prefer walking", "A jet maybe ?"]
print(f"Well owning a piece of {dream_vehicle[0].title()} has been a dream eversince i saw Sons of Anarchy")
print(f"I don't own cars yet but one day maybe I'll drive a James Bond's {dream_vehicle[1].title()} and take Dad around ")
print(f"ususally {dream_vehicle[2]}")
print(f"Well, God only knows about the future. I can own a {dream_vehicle[-1].lower()}")
names[2] = "Dash"
print(names)

#Addition of new elements 
dream_vehicle.append("Genie Mat")
print(dream_vehicle)

#Addition of new elements
shady_bikes = []
shady_bikes.append("Bajaj")
shady_bikes.append("Yamaha")
shady_bikes.append("TVS")
print(shady_bikes)

shady_bikes.insert(0, "Kawasaki")
print(shady_bikes)

#With insert, -1 refers to the second last instead of the last element. why ?
#Beacuse, it opens a space of the index -1 and shifts every other element a unit right
shady_bikes.insert(-1, 'Star')
print(shady_bikes)

#removing an item from the list. An encounter with statements in python
del names[2]
print(names)

#popping > deleting and using 
print(names.pop())
print(names)
#popping from a said position 
print(f"My best friend is {names.pop(0).title()}")
dream_vehicle.remove("Harley Davidson")
print(dream_vehicle)

unreal = "Genie Mat"
dream_vehicle.remove(unreal)

