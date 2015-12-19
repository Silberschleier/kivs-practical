import matplotlib.pyplot as plt
import sys
import time

seconds = []
datarate = []
sum = 0
i = 0
length = 1000

while True:                                 #Einlesen von stdin in Bloecken der Laenge length Bytes
    before = time.time()
    data = sys.stdin.read(length)
    seconds.append(time.time() - before)
    if len(data) == 0: break

for s in seconds:                           #Umrechnen von Sekunden pro Bytes in Bytes pro Sekunde
    sum += s
    i += 1
    if sum >= 1:
        datarate.append(length*i)
        sum = 0
        i = 0

plt.plot(seconds)
plt.savefig("seconds.png")
plt.close()
plt.plot(datarate)
plt.savefig("datarate.png")
plt.close()