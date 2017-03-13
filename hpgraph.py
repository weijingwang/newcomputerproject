from matplotlib import pyplot, dates
from csv import reader
from dateutil import parser

with open('table_hp.csv', 'r') as f:
    data = list(reader(f))

price = [i[5] for i in data[1::]]
time = [parser.parse(i[0]) for i in data[1::]]

pyplot.plot(time, price)
pyplot.show()