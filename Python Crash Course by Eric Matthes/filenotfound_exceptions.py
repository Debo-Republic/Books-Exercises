# Handling file not found exception :
file_name = 'alice.txt'
try:
    with open(file_name, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print("File doesn't exist in the directory!"
          " Please check and try again")
else:
    words = len(contents.split())
    print(f"The approximate number of words in the text is {words}")

