import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

#设置图表颜色有三种方法，一种是c='red',第二种是c=(0,0,0.8),第三种是颜色映射
plt.scatter(x_values, y_values, c=y_values, edgecolor='none', s=40)
plt.show()

#设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

#设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize=14)

#显示图像
#plt.show()

plt.savefig('squares_plot.png', bbox_inches='tight')

