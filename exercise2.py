import re
import statistics
import matplotlib.pyplot as plt
import argparse
import datetime
import time


def valid_date(string):
    if s == '':
        return time.time()
    return time.mktime(datetime.datetime.strptime(string, "%Y-%m-%d").timetuple())

parser = argparse.ArgumentParser(description='Aufgabe 2')
parser.add_argument('--low', type=valid_date, default='1970-01-01', help='YYYY-MM-DD')
parser.add_argument('--high', type=valid_date, default='', help='YYYY-MM-DD')
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

t = re.compile('\d+\n')                 # Einlesen des Zeitstempels
p = re.compile('time=(\d+\.\d+)')       # Einlesen der Roundtriptime
for line in f:
    if t.match(line) is not None:       # Erkennung von Zeitstempeln
        if int(line) > timestamp + c:
            sections.append(i)
        timestamp = int(line)
    m = p.findall(line)
    if m:
        if timeframeLow < timestamp < timeframeHigh:
            timestamp += 1
            timestamp_data.append(timestamp)
            ping_data.append(float(m[0]))
            i += 1

for s in range(1, len(sections)):                               # Daten fuer Boxplots aus Segmenten kopieren
    if s > len(sections):
        boxplot_data.append(ping_data[sections[s]:])
    else:
        boxplot_data.append(ping_data[sections[s-1]:sections[s]])

print "Minimum: ", min(ping_data)
print "Maximum: ", max(ping_data)
print "Mean: ", statistics.mean(ping_data)
print "Deviation: ", statistics.stdev(ping_data)

print "Sections:",
for s in sections:
    print timestamp_data[s],

plt.plot(timestamp_data, ping_data, 'x')
plt.xlabel("Time")
plt.ylabel("RTT")
plt.savefig("timestamp_data.png")
plt.close()

plt.boxplot(boxplot_data)
plt.ylabel("RTT")
plt.savefig("boxplot_data.png")
plt.close()

plt.plot(ping_data)
plt.xlabel("Seq.No.")
plt.ylabel("RTT")
plt.savefig("pingnr_data.png")
plt.close()