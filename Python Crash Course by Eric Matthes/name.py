name = "ada lovelace"
print(name.title())

print(name.upper())
print(name.lower())

first_name = "Debopriyo"
last_name = "Bhowmick"
full_name = f"{first_name} {last_name}"
print(full_name)

#utilising fstrings for multiple jobs
message = "It may be tough today, but one day you will win!"
print(f"God has a message for {first_name} {last_name} which goes as : {message.upper()} ")
print(f"{first_name} , speaking of God, what is the meaning of your name ? is it something like \t God's \t fav")
print(f"{full_name} List of technical skills: \n Python \n C \n R \n C++ \n Tableu")

#some real time input data cleaning tactics
year_2020 = " This year was a learning curve.   "
print(year_2020.strip())
print(year_2020.rstrip())
print(year_2020.lstrip())