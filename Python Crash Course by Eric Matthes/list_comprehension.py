even_squares = [value**2 for value in range(1,11,2)]
print(even_squares)

#Summing a million
one_mil = list(range(1,1000001))
print(min(one_mil))
print(max(one_mil))
print(sum(one_mil))

#odd game of numbers
odd_num = range(1,20,2)
for num in odd_num:
	print(num)

#multiples of 3 
mul = list(range(3,31,3))
for each in mul:
	print(each)


#Cubes of numbers 
cube = [val **3 for val in range(1,11)]
for num in cube:
	print(num)