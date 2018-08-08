import pygal

from random_walk import RandomWalk

rw = RandomWalk()

rw.fill_walk()

xy_chart = pygal.XY(stroke=False, show_x_labels=False)
xy_chart.title = 'Random Walk'

list_rw = []

for i in range(1,5000):
	points = (rw.x_values[i],rw.y_values[i])
	list_rw.append(points)
	
xy_chart.add('rw',list_rw)



xy_chart.render_to_file('pyg_rw.svg')


