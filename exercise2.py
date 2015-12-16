import re
import numpy
import statistics
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='bla')
parser.add_argument('--low', type=int, default=0)
parser.add_argument('--high', type=int, default=10000000000000000)
args = parser.parse_args()

ping_data = []
timestamp_data = []
sections = []
boxplot_data =[]
timestamp = 0
c = 500000
i = 0

timeframeLow = args.low
timeframeHigh = args.high

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
        if timestamp > timeframeLow and timestamp < timeframeHigh:
            timestamp += 1
            timestamp_data.append(timestamp)
            ping_data.append(float(m[0]))
            i += 1

for s in range(1, len(sections)):
    if (s) > len(sections):
        boxplot_data.append(ping_data[sections[s]:])
    else:
        boxplot_data.append(ping_data[sections[s-1]:sections[s]])
print "Minimum: ", min(ping_data)
print "Maximum: ", max(ping_data)
print "Mean: ", numpy.mean(ping_data)
print "Deviation: ", statistics.stdev(ping_data)

print len(ping_data)

print sections

#print boxplot_data[2]


plt.plot(timestamp_data, ping_data, 'bs')
plt.savefig("timestamp_data.png")
plt.boxplot(boxplot_data)
plt.savefig("boxplot_data.png")
plt.plot(boxplot_data[1])
plt.savefig("pingnr_data.png")