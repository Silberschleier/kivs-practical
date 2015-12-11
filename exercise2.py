import re
import numpy
import statistics
import matplotlib.pyplot as plt
f = open('PA.log', 'r')
data = []
timestamp = []

p = re.compile('time=(\d+\.\d+)')
for line in f:
    m = p.findall(line)
    if m:
        data.append(float(m[0]))

p = re.compile('time=(\d+\\PING)', re.MULTILINE)
for line in f:
    m = p.findall(line)
    if m:
        timestamp.append(float(m[0]))

print "Minimum: ", min(data)
print "Maximum: ", max(data)
print "Mean: ", numpy.mean(data)
print "Deviation: ", statistics.stdev(data)

plt.plot(data)
plt.show()