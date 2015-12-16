import re
import statistics
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='aufgabe2')
parser.add_argument('--low', type=int, default=0)
parser.add_argument('--high', type=int, default=10000000000000000)
args = parser.parse_args()

ping_data = []
timestamp_data = []
sections = []
boxplot_data =[]
timestamp = 0
c = 500000                      #Minimaler Abstand zweier Segmente
i = 0

timeframeLow = args.low         #Zeitfenster, das betrachtet werden soll
timeframeHigh = args.high

contents = ""
f = open('PA.log', 'r')

t = re.compile('\d+\n')                 #Einlesen des Zeitstempels
p = re.compile('time=(\d+\.\d+)')       #Einlesen der Roundtriptime
for line in f:
    if t.match(line) is not None:       #Erkennung von Zeitstempeln
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

for s in range(1, len(sections)):                                #Auswertung der Pingdaten
    if (s) > len(sections):
        boxplot_data.append(ping_data[sections[s]:])
    else:
        boxplot_data.append(ping_data[sections[s-1]:sections[s]])
print "Minimum: ", min(ping_data)
print "Maximum: ", max(ping_data)
print "Mean: ", statistics.mean(ping_data)
print "Deviation: ", statistics.stdev(ping_data)

print "Sections: ", sections

plt.plot(timestamp_data, ping_data, 'bs')
plt.savefig("timestamp_data.png")
plt.boxplot(boxplot_data)
plt.savefig("boxplot_data.png")
plt.plot(boxplot_data[1])
plt.savefig("pingnr_data.png")