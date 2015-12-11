import re
import numpy
import statistics
import matplotlib.pyplot as plt
ping_data = []
timestamp_data = []

contents = ""
f = open('PA.log', 'r')

t = re.compile('\d+\n')
p = re.compile('time=(\d+\.\d+)')
for line in f:
    if t.match(line) is not None:
        timestamp = int(line)
    m = p.findall(line)
    if m:
        timestamp += 1
        timestamp_data.append(timestamp)
        ping_data.append(float(m[0]))

print "Minimum: ", min(ping_data)
print "Maximum: ", max(ping_data)
print "Mean: ", numpy.mean(ping_data)
print "Deviation: ", statistics.stdev(ping_data)

plt.plot(timestamp_data, ping_data, 'bs')
plt.show()