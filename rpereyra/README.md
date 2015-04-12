Neighborhoods.py

This file reads a sample dataset of the format described in the README at the root of this repository and, after decoupling on Harris Teeter ticket ID, appends a column to the dataset comprised of an integer value denoting the rows' "neighborhood". The neighborhood is defined by a k-means algorithm which groups clusters of geospatial coordinates (latitude and longitude). In this particular case, the coordinates represent estimated locations of customer homes, calculated by averaging the coordinates of the locations of the intersections between the customer's home radius from their home store and the vector between the customer's home store and any given store where they made a purchase.

Store_Hour.py

Map Reduce approach to determine activity by hour of the day for each neighborhood. See README in the spark directory for more information.

Visualization.py

Generates a heatmap for neighborhoods' activity (number of purchases in a given hour). Hour of the day along the X-axis and neighborhood ID along the Y.

Visualization2.py

Plots on an X-Y plane (longitude, latitude) the estimated locations of customer homes + the centroids of the k-means algorithm applied in Neighborhoods.py
