fav_prog_lang = {
	'debo': ['R', 'Python'],
	'Mayuri' : ['Salesforce', 'Linux', 'Python'],
	'Jaison' : ['Ruby', 'Go' , 'HTML', 'CSS'],
	'Dash' : ['Python', 'SQL', 'R']
}

#Printing everyones favourite language 
for name, languages in fav_prog_lang.items():
	print(f" \n{name.title()} like to work with the following programming languages:")
	for language in languages:
		print(f"{language.title()}")

#Printing all favourite languages mentioned : 
