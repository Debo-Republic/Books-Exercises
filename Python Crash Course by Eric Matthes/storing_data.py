# using json.dump() and json.load()
import json

numbers = [1,2,3,4,5,67]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

filename = 'numbers.json'
with open(filename) as f:
    yo = json.load(f)

print(yo)