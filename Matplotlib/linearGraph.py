# Using Matplotlib to plot a Linear Graph
import matplotlib.pyplot as plt
x = [1, 2, 3]
y = [1, 4, 9]
z = [10, 0, 5]

plt.plot(x, y, label='This is Y')
plt.plot(x, z, label='This is Z')
plt.title('Test Plot')
plt.xlabel('X')
plt.ylabel('Y and Z')

# Using args in plt.legend without arg label in plt.plot (Error prone!)
# plt.legend(['This is Y', 'This is Z'])

plt.show()
