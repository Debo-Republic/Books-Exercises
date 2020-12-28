# Handling exceptions while working with multiple files.
def count(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print("File doesn't exist in the directory!"
              " Please check and try again")
    else:
        words = len(contents.split())
        print(f"The approximate number of words in the {filename} is {words}")


file_names = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for file_name in file_names:
    count(file_name)

