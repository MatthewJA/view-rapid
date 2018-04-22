import collections

import matplotlib.pyplot as plt
import numpy
import pandas

stops = pandas.read_csv('stops.txt')
stops.set_index('stop_id', inplace=True)
stop_names = stops['stop_name'].to_dict()
stop_lats = stops['stop_lat'].to_dict()
stop_lons = stops['stop_lon'].to_dict()

times = pandas.read_csv('stop_times.txt')
weekday = times['trip_id'].str.contains('Weekday')

def plot_stops(stops, cmap):
    stop_counts = collections.Counter(stops)
    lons = []
    lats = []
    names = []
    importances = []
    for i, count in stop_counts.most_common():
        lons.append(stop_lons[i])
        lats.append(stop_lats[i])
        names.append(stop_names[i])
        importances.append(count / 10)

    plt.scatter(lons, lats, s=importances, edgecolor='None', c=importances,
                cmap=cmap)

plot_stops(times['stop_id'][weekday], 'winter')
plot_stops(times['stop_id'][~weekday], 'summer')

plt.gca().set_aspect('equal')
plt.show()
