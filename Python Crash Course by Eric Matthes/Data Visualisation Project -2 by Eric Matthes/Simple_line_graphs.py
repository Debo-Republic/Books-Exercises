# Drawing simple line graphs.

import matplotlib.pyplot as plt
input_values = range(1, 11)
squares = [value**2 for value in range(1, 11)]
print(squares)
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=4)

# Cosmetic changes to the plot
ax.set_title("Square of numbers!", fontsize=24)
ax.set_xlabel("Numbers", fontsize=14)
ax.set_ylabel("Values", fontsize=14)
ax.tick_params(axis='both', labelsize=14)
plt.show()
plt.clf()