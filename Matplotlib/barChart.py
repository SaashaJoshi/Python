# Using matplotlib to plot Bar Chart
import numpy as np
from matplotlib import pyplot as plt

plt.xkcd()
x = [1, 2, 3, 4, 5, 6]
y = [8, 14, 19, 25, 24, 32]
z = [10, 18, 25, 28, 30, 40]
w = [4, 8, 16, 18, 20, 24]

x_indices = np.arange(len(x))
width=0.25

plt.bar(x_indices-width, y, color='#444444', width=width, label='This is Y')
plt.bar(x_indices, z, color='#008fd5', width=width, label='This is Z')
plt.bar(x_indices+width, w, color='#ffd700', width=width, label='This is W')

plt.xticks(ticks=x_indices, labels=x)	# Replacing tick (indices) location with appropriate labels

plt.title('Test Plot')
plt.xlabel('X')
plt.ylabel('Y and Z')
plt.legend()
plt.show()