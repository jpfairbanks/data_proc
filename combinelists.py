from string import join
from datetime import datetime

def get_between(string, sep1, sep2):
    tmp = string.split(sep1)[1]
    return tmp.split(sep2)[0]

ids = file('ids.txt', 'r')
names = file('titles.txt', 'r')
times = file('times.txt', 'r')
outf = file('edges.csv', 'w')

for iline in ids:
    nameline = names.readline()
    timeline = times.readline()
    lines = (iline, nameline, timeline)
    _id, _name, timestr = [get_between(l, '>', '<') for l in lines]
    dttime = (datetime.strptime(timestr, '%Y-%m-%dT%H:%M:%SZ'))
    _time = dttime.strftime('%s')
    combline = join([_id, _name, _time, '\n'], ',')
    outf.write(combline)

[f.close() for f in (ids, names, outf)]
