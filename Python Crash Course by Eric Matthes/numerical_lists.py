#Off by one behaviour in for loop 
for num in range(1,5):
	print(num)
for you in range(6):
	print(you)

print(range(6))
#Using range to create lists 
print(list(range(6)))
#creating a list of even numbers 
even_numbers = list(range(2,11,2))
print(f"Even numbers from 2 to 10 are {even_numbers}")
squared = []
for num in range(1,11):
	squared.append(num**2)
	print(num**2)
	print(squared)