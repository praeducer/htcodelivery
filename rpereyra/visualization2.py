import matplotlib.pyplot as plt
import string
import numpy as np
import csv
import matplotlib.pyplot as plt

with open('out_full2.bsv', 'rb') as bsvfile:
    data_rows = csv.DictReader(bsvfile, delimiter='|')
    to_keep = []
    for data in data_rows:
        to_keep.append(data)
    x_cust = []
    y_cust = []
    cx = []
    cy = []
    for data in to_keep:
        x_cust.append(-1.0 * float(data['LonInt']))
        y_cust.append(float(data['LatInt']))
        cx.append(-1.0 * float(data['z_CenLon']))
        cy.append(float(data['z_CenLat']))

    plt.plot(x_cust, y_cust, 'ro')
    plt.plot(cx, cy, 'bo')
    plt.axis([-81.1, -80.45, 35.0, 35.4])
    plt.savefig('map.png', transparent=True)