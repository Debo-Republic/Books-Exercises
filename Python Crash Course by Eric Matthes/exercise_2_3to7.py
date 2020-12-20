full_name = "Mayuri B Upadhaya"
print(f"Hello {full_name}, would you like to learn some python today ?")

#name cases 
another_name = "guess who's back"
print(another_name.lower())
print(another_name.upper())
print(another_name.title())

#Famous quote 
quote = "You must go into the unknown, kill the part of yourself that doesn't help you.\n Rescue your father from the dead and take the path that God has laid out."
person = "\tJordan B. Peterson \n"

print(f'{person.strip()} famously said "{quote}"')
#Strip only sstrips the first and the last whitespaces, Whitespaces in between isn't counted as whitespace. 
person = "\tJordan \n B. \t Peterson \n"
print(person.strip())