from itertools import groupby
import pygal
def draw_line(x_data, y_data, title, y_legend):
	xy_map = []
	for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
		y_list = [v for _, v in y]
		xy_map.append([x, sum(y_list) / len(y_list)])
	x_unique, y_mean = [*zip(*xy_map)]
	line_chart = pygal.Line()
	line_chart.title = title
	line_chart.x_labels = x_unique
	line_chart.add(y_legend, y_mean)
	line_chart.render_to_file(title+'.svg')
	return line_chart
	
