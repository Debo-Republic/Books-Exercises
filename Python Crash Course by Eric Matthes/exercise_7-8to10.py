#deli:

sandwich_orders = ['chicken_sub', 'veggie_sub', 'ceaser_sb', 'greek_sub', 'pastarami', 'pastarami', 'pastarami']
finished_sandwiches =[]

for sandwich in sandwich_orders:
    print(f"Your delicious {sandwich} is ready.")
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)

#No pastarami
while('pastarami' in sandwich_orders):
    sandwich_orders.remove('pastarami')

print(sandwich_orders)

#Dream vacations :

poll = True
dream_vacation = {}
prompt_1 = "\n Hi ! type in your username!"
prompt_2 = "Tell me your dream vacation."
prompt_3 = "Would you like to continue playing ? Y/N"
while poll:
    name = input(prompt_1)
    response = input(prompt_2)
    dream_vacation[name] = response
    repeat = input(prompt_3)
    if repeat == 'N':
        poll = False
print(f"The user destination data that has been collected is {dream_vacation}")

