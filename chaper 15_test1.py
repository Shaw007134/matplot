import matplotlib.pyplot as plt

x1 = list(range(1,5))
y1 = [x**3 for x in x1]

plt.scatter(x1,y1,s=40,c=y1,cmap=plt.cm.Blues,edgecolor='none')

plt.show()

x2 = list(range(1,5000))
y2 = [x2**3 for x2 in x2]

plt.scatter(x2,y2,s=40,c=y2,edgecolor='none')

plt.show()
