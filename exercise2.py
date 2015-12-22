import re
import statistics
import matplotlib.pyplot as plt
import argparse
import datetime
import time


def valid_date(string):
    if string == '':
        return time.time()
    return time.mktime(datetime.datetime.strptime(string, "%Y-%m-%d").timetuple())

parser = argparse.ArgumentParser(description='Aufgabe 2')
parser.add_argument('--low', type=valid_date, default='1970-01-01', help='YYYY-MM-DD')
parser.add_argument('--high', type=valid_date, default='', help='YYYY-MM-DD')
parser.add_argument('--segthresh', type=int, default=5000000, help='Zeit in Sekunden')
args = parser.parse_args()

ping_data = []
timestamp_data = []
sections = []
boxplot_data = []
timestamp = 0
c = args.segthresh                      #Minimaler Abstand zweier Segmente (default ca. 2 Monate)
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


# Daten fuer Boxplots aus Segmenten kopieren
for s in range(0, len(sections)):
    if s >= len(sections)-1:
        boxplot_data.append(ping_data[sections[s]:])
    else:
        boxplot_data.append(ping_data[sections[s]:sections[s+1]])


print "Minimum: ", min(ping_data)
print "Maximum: ", max(ping_data)
print "Mean: ", statistics.mean(ping_data)
print "Deviation: ", statistics.stdev(ping_data)

print "Sections:",
for s in sections:
    print timestamp_data[s],

plt.plot(timestamp_data, ping_data, '.')
plt.xlabel("Time")
plt.ylabel("RTT")
for s in sections:
    plt.axvline(timestamp_data[s], color='r', linestyle='--')
plt.savefig("timestamp_data.png")
plt.close()

plt.boxplot(boxplot_data)
plt.ylabel("RTT")
plt.savefig("boxplot_data.png")
plt.close()

plt.plot(ping_data)
plt.xlabel("Seq.No.")
plt.ylabel("RTT")
for s in sections:
    plt.axvline(s, color='r', linestyle='--')
plt.savefig("pingnr_data.png")
plt.close()