import matplotlib.pyplot as plt
import sys
import time

seconds = []
datarate = []
time_sum = 0
i = 0
length = 1024

while True:                                 #Einlesen von stdin in Bloecken der Laenge length Bytes
    before = time.time()
    data = sys.stdin.read(length)
    seconds.append(time.time() - before)
    if len(data) == 0: break

for s in seconds:                           #Umrechnen von Sekunden pro Bytes in Bytes pro Sekunde
    time_sum += s
    i += 1
    if time_sum >= 1:
        datarate.append(i)
        time_sum = 0
        i = 0

plt.style.use("bmh")

plt.plot(seconds)
plt.ylabel("Seconds")
plt.xlabel("KBytes")
plt.savefig("seconds.pdf")
plt.close()

plt.plot(datarate)
plt.ylabel("KB/s")
plt.xlabel("Seconds")
plt.savefig("datarate.pdf")
plt.close()