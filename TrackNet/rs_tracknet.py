import csv
import queue
import numpy as np
import sys

input_csv_name = sys.argv[1]
output_filename = sys.argv[2]

q = queue.Queue(maxsize=2)
a = []
for i in range(30):
    a.append(0)

with open(input_csv_name, newline='') as file:
    rows = csv.reader(file)
    playing = 0
    start = 0
    end = 0
    count_visible = 0
    count_invisible = 0
    infos = [[0, 0]]
    ishigh = 0
    temp = 0
    isheader = 1
    for row in rows:
        if isheader == 1:
            isheader = 0
            continue
        if playing == 0:
            a.pop(0)
            a.append(int(row[1]))
            if sum(a) >= 22:
                data = []
                start = int(row[0]) - 50
                playing = 1
        else:
            a.pop(0)
            a.append(int(row[1]))
            if int(row[1]) == 1:
                if q.qsize() == 2:
                    q.get()
                q.put(int(row[3]))
            if sum(a) <= 8:
                playing = 0
                s = 0
                while not q.empty():
                    n = q.get()
                    s += n
                if s/2 <= 150:
                    temp = start
                    ishigh = 1
                else:
                    if ishigh == 1:
                        start = temp
                        ishigh = 0
                    end = int(row[0]) + 15
                    infos = np.append(infos, [[start, end]], axis=0)


with open(output_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Start', 'End'])
    for info in infos:
        if info[0] == 0:
            continue
        writer.writerow(info)