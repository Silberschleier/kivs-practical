import numpy
import statistics
import matplotlib.pyplot as plt
import sys
import time
import threading

data = []
done = False
sum = 0

def read_data():
    global sum
    for line in sys.stdin:
        sum += len(line)

def time_measure():
    global sum
    global done
    while not done:
        time.sleep(1)
        data.append(sum)
        print sum
        sum = 0

t1 = threading.Thread(target=read_data())
t2 = threading.Thread(target=time_measure())

t1.start()
t2.start()
t1.join()
done = True

plt.plot(data)
plt.show()