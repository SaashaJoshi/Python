import matplotlib.pyplot as plt

labels = 'LINEAR ALGEBRA', 'PROBABILITY THEORY AND STATISTICS', 'CALCULUS', 'ALGORITHMS AND COMPLEXITY', 'DATA PRE-PROCESSING'
sizes = [35, 25, 15, 15, 10]
colors=['#581845', '#900C3F', '#C70039', '#FF5733', '#FFC300']
#explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice 

plt.pie(sizes, labels=labels, colors=colors, startangle=180, autopct='%.1f%%')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
