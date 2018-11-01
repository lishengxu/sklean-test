from sklearn.cluster import KMeans
import numpy as np

x = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])

kmeans = KMeans(n_clusters = 2, random_state = 0).fit(x)

print "labels:", kmeans.labels_

print "predict:", kmeans.predict([[0, 0], [4, 4]])

print "center:", kmeans.cluster_centers_