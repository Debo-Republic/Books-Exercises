cars = ['BMW', 'Mercedes', 'Tesla', 'Honda']
print(cars.sort())
cars.append("Hyundai")
print(sorted(cars, reverse = True))
cars.reverse()
print(cars)


dream_places = ["oregon", "amsterdam", "kalahari", "california", "gokarna"]
#Print as a raw python list 
print(dream_places)
#printing as a temporary sorted list 
print(sorted(dream_places))
#Found - sorting has issues with uper and lower cases prints. Important to maintain consistency in data 
print(dream_places)
#Use reverse in sorted function 
print(sorted(dream_places, reverse = True))
#Show that original structure is maintained in a list 
print(dream_places)
dream_places.reverse()
print(dream_places)
dream_places.reverse()
print(dream_places)
dream_places.sort()
print(dream_places)
dream_places.sort(reverse = True)

#printing the length of the list 
print(len(dream_places))