import matplotlib.pyplot as plt
import string
import numpy as np
import csv
import matplotlib.pyplot as plt

activities = open('reduce_output.txt', 'rb')

inrows = []
for activity in activities:
    inrows.append(string.split(activity, '|'))

hoods = {}
i = 0
for row in inrows:
    j = int(row[0])
    if j in hoods.keys():
        continue
    hoods[int(row[0])] = i
    i = i + 1

inrows2 = []
i = 0
for row in inrows:
    inrows2.append([])
    inrows2[i].append(hoods[int(row[0])])
    inrows2[i].append(int(row[1].strip()))
    inrows2[i].append(float(row[2].strip()))
    i = i + 1

output = np.zeros((len(hoods),24))

for activity in inrows2:
    output[int(activity[0])][int(activity[1])] = np.log(float(activity[2]))

plt.pcolor(output,cmap=plt.cm.Reds,edgecolors='k')
plt.savefig('time.png')