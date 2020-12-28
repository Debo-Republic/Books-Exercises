# Reading from a file from the same directory in the program
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.strip())

# Reading programs from a different directory
with open('C:\\Users\\Kushal Bhowmick\\Desktop\\career\\Skill Sets\\Python\\Python Crash Course by Eric Matthes'
          '\\ehmatthes-pcc_2e-078318e\\chapter_10\\pi_digits.txt') as same_objects:
    for line in same_objects:
        print(line.strip())

# Reading programs line by line into a variable.
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

# Reading a self made file from the present directory.
# Reading the entire file and printing.
with open('learning_python.txt') as file_object:
    contents = file_object.read()
print(contents)
print("This was called Reading the entire file and printing.\n")

# Printing by looping over the contents line by line.
with open('learning_python.txt') as file_object:
    for line in file_object:
        print(line.strip())
        print("Print another line.")
print("Printing by looping over the contents line by line.\n")

# Printing by reading line by line and printing.
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())
    print("Print another line.")
print("Printing by reading line by line and printing.\n")

# Reading and replacing data from strings.
message = "I freaking love poodles."
print(message.replace('poodles', 'maine coon'))

# Read an object line by line and start replacing words in the object.
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.replace('python', 'ruby on rails.'))
