import matplotlib.pyplot as plt
import sys
import time

seconds = []
datarate = []
sum = 0
i = 0
a = 1000

while True:
    before = time.time()
    data = sys.stdin.read(a)
    seconds.append(time.time() - before)
    if len(data) == 0: break

for s in seconds:
    sum += s
    i += 1
    if sum >= 1:
        datarate.append(a*i)
        sum = 0
        i = 0

plt.plot(seconds)
plt.savefig("seconds.png")
plt.plot(datarate)
plt.show()
plt.savefig("datarate.png")