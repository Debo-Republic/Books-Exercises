# Program that explores all built in style of matplotlib styles

import matplotlib.pyplot as plt
print(plt.style.available)

input_value = range(1, 12)
output_value = [value**value for value in range(1, 12)]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_value, output_value, linewidth=2)
plt.show()


