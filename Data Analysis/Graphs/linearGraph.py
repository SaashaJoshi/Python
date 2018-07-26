import matplotlib.pyplot as plt
import pandas as pd

x = [1, 2, 3]
y = [1, 4, 9]
z = [10, 0, 5]
plt.plot(x, y)
plt.plot(x, z)

plt.title('Test Plot')

plt.xlabel('X')
plt.ylabel('Y and Z')

plt.legend(['This is Y', 'This is Z'])
plt.show()
