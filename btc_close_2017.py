#~ from __future__ import (absolute_import, division, print_function, unicode_literals)

#~ try:
	#~ # Python 2.x version
	#~ from urllib2 import urlopen
#~ except ImportError:
	#~ # Python 3.x version
	#~ from urllib.request import urlopen
#~ import json

#~ json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
#~ response = urlopen(json_url)
#~ # read data
#~ req = response.read()

#~ # write the data into file
#~ with open('btc_close_2017_urllib.json','wb') as f:
	#~ f.write(req)
#~ # load json format
#~ file_urllib = json.loads(req)
#~ print(file_urllib)

#~ import requests
#~ json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
#~ req = requests.get(json_url)
#~ # write the data into the file
#~ filename = 'btc_close_2017_request.json'
#~ with open('btc_close_2017_request.json','w') as f:
	#~ f.write(req.text)
#~ file_requests = req.json()

filename = 'btc_close_2017.json'
#print(file_requests)
import json
with open(filename) as f:
	btc_data = json.load(f)
#print each day information
# create 5 lists and store the date as well as the close price
dates = []
months = []
weeks = []
weekdays = []
close = []
for btc_dict in btc_data:
	dates.append(btc_dict['date'])
	months.append(int(btc_dict['month']))
	weeks.append(int(btc_dict['week']))
	weekdays.append(btc_dict['weekday'])
	close.append(int(float(btc_dict['close'])))
	#print("{} is month {} week {}, {}, the close price is {} RMB".format(date, month, week, weekend, close))
	
import pygal 
import math
#~ line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
#~ line_chart.title = 'close price (RMB) '
#~ line_chart.x_labels = dates
#~ N = 20 # interval for dates is 20
#~ line_chart.x_labels_major = dates[::N]
#~ line_chart.add('Close Price', close)
#~ line_chart.render_to_file('Close price plot for btc(RMB).svg')

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = 'close price log reverse (RMB) '
line_chart.x_labels = dates
N = 20 # interval for dates is 20
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
line_chart.add('Close Price', close_log)
line_chart.render_to_file('Close price plot for btc(RMB) log .svg')

from draw_line import draw_line

#~ idx_month = dates.index('2017-12-01')
#~ line_chart_month = draw_line(months[:idx_month],close[:idx_month], 'close price month day avg(RMB)','month day avg value')
#~ line_chart_month

idx_week = dates.index('2017-12-11')
#~ line_chart_week = draw_line(weeks[1:idx_week], close[1:idx_week], 'close price sunday avg(RMB)', 'sunday avg value')
#~ line_chart_week

#~ wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#~ weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
#~ line_chart_weekday = draw_line(weekdays_int, close[1:idx_week], 'close price week avg(RMB)', 'week avg value')

with open('close price Dashboard.html', 'w', encoding='utf-8') as html_file:
	html_file.write('<html><head><title>close price dashboard</title><meta charset="utf-8"></head><body>\n')
	for svg in [
		'Close price plot for btc(RMB).svg', 'Close price plot for btc(RMB) log .svg', 'close price month day avg(RMB).svg',
		'close price sunday avg(RMB).svg', 'close price week avg(RMB).svg'
		]:
			html_file.write('	<object type="image/svg+xml" data="{0}" height = 500></object>\n'.format(svg))
			html_file.write('</body></html>')
