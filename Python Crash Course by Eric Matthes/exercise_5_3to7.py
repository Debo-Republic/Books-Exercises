#IFs, elifs and multiple ifs
alien_colors = ['red', 'green', 'blue', 'yellow']
if ('green' in alien_colors):
	print("You just earned 5 freaking points for saving the humanity")

if ('black' in alien_colors):
	print("You just earned 5 freaking points for saving the humanity")
else:
	print('oopsie dasiy. You did not manage to kill the real alien.')

alien_shot = 'green'

if (alien_shot in alien_colors):
	print("You just earned 5 freaking points for saving the humanity")
else:
	print("You just earned 10 points for failing. Keep failing.")