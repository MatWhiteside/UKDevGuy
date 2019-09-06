import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans

data, labels = make_blobs(n_samples=120, centers=3, random_state=42)

# Initialise k-means
kmeans = KMeans(n_clusters=3).fit(data)
cluster_labels = kmeans.predict(data)

# Plot the results of clustering
plt.title('Clustered Data')
plt.scatter(data[:,0], data[:,1], c=cluster_labels)
plt.show()






