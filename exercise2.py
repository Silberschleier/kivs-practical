import re
import numpy
import statistics
import matplotlib.pyplot as plt
ping_data = []
timestamp_data = []
sections = []
boxplot_data =[]
timestamp = 0
c = 500000
i = 0

contents = ""
f = open('PA.log', 'r')

t = re.compile('\d+\n')
p = re.compile('time=(\d+\.\d+)')
for line in f:
    if t.match(line) is not None:
        if int(line) > timestamp + c:
            sections.append(i)
        timestamp = int(line)
    m = p.findall(line)
    if m:
        timestamp += 1
        timestamp_data.append(timestamp)
        ping_data.append(float(m[0]))
        i += 1

for s in range(1, len(sections)-1):
    if (s+1) > len(sections)-1:
        boxplot_data.append(ping_data[sections[s]:])
    else:
        boxplot_data.append(ping_data[sections[s-1]:sections[s]])

print "Minimum: ", min(ping_data)
print "Maximum: ", max(ping_data)
print "Mean: ", numpy.mean(ping_data)
print "Deviation: ", statistics.stdev(ping_data)

#plt.plot(timestamp_data, ping_data, 'bs')
#plt.boxplot(boxplot_data)
plt.plot(boxplot_data[2])
plt.show()