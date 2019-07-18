# Using Matplotlib to plot a Linear Graph
import matplotlib.pyplot as plt

#plt.style.use('ggplot')	# Use print(plt.style.available) to print out the available styles
plt.xkcd()	# Mimics the style of a comic magazine!
x = [1, 2, 3, 4, 5, 6]
y = [8, 14, 19, 25, 24, 32]
z = [10, 18, 25, 28, 30, 40]

plt.plot(x, y, label='This is Y')
plt.plot(x, z, label='This is Z')
plt.title('Test Plot')
plt.xlabel('X')
plt.ylabel('Y and Z')
plt.legend()
'''
Using args in plt.legend without arg label in plt.plot (Error prone!)
plt.legend(['This is Y', 'This is Z'])
'''
plt.grid(True)
plt.tight_layout()	# Provides padding
#plt.savefig('plot.png')	Saves the plot in the working directory else mention a path
plt.show()