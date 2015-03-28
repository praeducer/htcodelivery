import numpy as np
import numpy.linalg as la
import csv
from sklearn.cluster import MiniBatchKMeans

def _init_():
    with open('sample.bsv', 'rb') as bsvfile:
        data_rows = csv.DictReader(bsvfile, delimiter='|')
        to_keep = []
        for data in data_rows:
            lon_int, lat_int = find_intersections(data)
            data['LonInt'] = lon_int
            data['LatInt'] = lat_int
            to_keep.append(data)
        decoupled_data = decouple(to_keep)
        kmeans_data = kmeans(decoupled_data)
        to_file(kmeans_data)

def find_intersections(data):
    homeStoreLon = -1.0 * float(data['homeStoreLon']) / 180.0 * np.pi
    homeStoreLat = float(data['homeStoreLat']) / 180.0 * np.pi
    storeLon = -1.0 * float(data['storeLon']) / 180.0 * np.pi
    storeLat = float(data['storeLat']) / 180.0 * np.pi
    distance = float(data['distance'])
    R = 3959.0

    if homeStoreLon == storeLon and homeStoreLat == storeLat:
        return homeStoreLon, homeStoreLat

    v1 = np.array([homeStoreLon, homeStoreLat])
    v2 = np.array([storeLon, storeLat])
    cosang = np.dot(v1, v2)
    sinang = la.norm(np.cross(v1, v2))
    tc = np.arctan2(sinang, cosang)

    lat = np.arcsin(np.sin(homeStoreLat) * np.cos(distance/R) + np.cos(homeStoreLat) * np.sin(distance/R) * np.cos(tc))
    lon = homeStoreLon + np.arctan2(np.sin(tc) * np.sin(distance/R) * np.cos(homeStoreLat), np.cos(distance/R) - np.sin(homeStoreLat) * np.sin(lat))

    lat = lat * 180.0 / np.pi
    lon = lon * 180.0 / np.pi

    return lon, lat

def decouple(data_rows):
    to_return = []
    receipts = []
    for data in data_rows:
        if data['receipt'] not in receipts:
            receipts.append(data['receipt'])
            to_return.append(data)
    return to_return

def kmeans(data_rows):
    X = []
    for data in data_rows:
        X.append([data['LonInt'], data['LatInt']])
    c = 60
    k_means = MiniBatchKMeans(n_clusters=c, batch_size=c*5)
    k_means.fit(X)
    print 'K Means Inertia: ' + str(k_means.inertia_)
    for i, data in enumerate(data_rows):
        data['Cluster'] = k_means.labels_[i]
        data['z_CenLat'] = k_means.cluster_centers_[k_means.labels_[i]][1]
        data['z_CenLon'] = k_means.cluster_centers_[k_means.labels_[i]][0]
    return data_rows

def to_file(data_rows):
    with open('out_full2.bsv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerow(data_rows[0].keys())
        for data in data_rows:
            writer.writerow(data.values())

_init_()