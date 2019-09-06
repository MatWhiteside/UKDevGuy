import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.cluster import KMeans

# Generate data
data, labels = make_blobs(n_samples=120, centers=3, random_state=42)

# Define large number of iterations so it doesn't play
# a factor in deciding k
iterations = 300

# Define lists that will populate our x, y axes
x = []
ssd_list = []

# Repeat the algorithm for k = 1..10
for k in range(1, 11):
    x.append(k)
    # Randomly initialise k centroids
    centroids, c_labels = make_blobs(n_samples=k, centers=k, random_state=42)

    # Repeat asssigning and recalculation of centroids
    for i in range(0, iterations):
        # Calculate distances
        dists = euclidean_distances(data, centroids)
        
        # Get the index of the closest cluster for each
        # data point
        predicted_label = np.argmin(dists, axis=1)

        # Recalculate the centroids
        new_centroids = np.zeros(shape=[k,data.shape[1]])
        for centroid in range(0, centroids.shape[0]):
            # Get all datapoints alocated to cluster 
            cluster_data = data[predicted_label == centroid]
            # Calculate the mean of this cluster
            if len(cluster_data) > 0:
                new_centroids[centroid, :] = np.mean(cluster_data, axis=0)
            else:
                new_centroids[centroid, :] = centroids[centroid, :]
            
        # Assign the new cluster centers
        centroids = new_centroids

    # Calculate SSD
    ssd = 0
    for i in range(0, 120):
        ssd += dists[i][predicted_label[i]]**2
    # Append SSD to y axis data
    ssd_list.append(ssd)

# Plot the results
plt.title("Own implementation SSD")
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.xlabel("k")
plt.ylabel("Sum of Squared Distances")
plt.plot(x, ssd_list, 'o-')
plt.show()

# Define data
data, labels = make_blobs(n_samples=120, centers=3, random_state=42)
# Empty data for y axis
ssd_list = []
# Repeat the algorithm for k = 1..10
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k).fit(data)
    cluster_labels = kmeans.predict(data)
    # Append SSD to y axis data
    ssd_list.append(kmeans.inertia_)

# Plot results
plt.title("Scikit-learn implementation SSD")
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.xlabel("k")
plt.ylabel("Sum of Squared Distances")
plt.plot(x, ssd_list, 'o-')
plt.show()
    


