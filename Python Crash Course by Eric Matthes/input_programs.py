#multiples of 10
message = "Check visibility by 10!"
message += "Give me a natural number."
num = int(input(message))
if num%10 == 0:
    print(f"the {num} is divisible by 10.")
else:
    print(f"the {num} is not divisible by 10.")