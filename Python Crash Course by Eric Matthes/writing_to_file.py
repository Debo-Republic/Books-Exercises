# Creating and writing to a text file.

file_name = 'yolo.txt'
with open(file_name, 'w') as file_object:
    file_object.write('I freaking love programming.')

with open(file_name) as file_object:
    print(file_object.read())

# Using newline character to write over multiple lines.
with open(file_name, 'w') as file_object:
    file_object.write("I love programming. \n")
    file_object.write("Python is my favourite language. \n")

with open(file_name, 'r') as file_object:
    print(file_object.read())

# Using append mode to add to the existing contents in the file.
with open(file_name, 'a') as file_object:
    file_object.write("\n I find meanig in working with large datasets.")
    file_object.write("\n I also love creating applications that can work in the browser!")

