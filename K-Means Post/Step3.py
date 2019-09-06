import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.metrics.pairwise import euclidean_distances

# Generate data
data, labels = make_blobs(n_samples=120, centers=3, random_state=42)

# Define k and centroids
k = 3
centroids = np.array([[-5,-5], [0,0], [5,5]])

# Calculate distances
dists = euclidean_distances(data, centroids)

# Get the index of the closest cluster for each
# data point
predicted_label = np.argmin(dists, axis=1)

# For each cluster, draw lines to their data points
for i in range(0, 120):
    if predicted_label[i] == 0:
        plt.plot([data[i][0], centroids[0][0]], [data[i][1], centroids[0][1]], linewidth=0.5, color="#44015433")
    elif predicted_label[i] == 1:
        plt.plot([data[i][0], centroids[1][0]], [data[i][1], centroids[1][1]], linewidth=0.5, color="#21918c33")
    elif predicted_label[i] == 2:
        plt.plot([data[i][0], centroids[2][0]], [data[i][1], centroids[2][1]], linewidth=0.5, color="#fde72533")

# Plot the data
plt.scatter(data[:,0], data[:,1], c=predicted_label)
# Plot the cluster centroids on top
plt.scatter(centroids[:,0], centroids[:,1], marker="x", color="red")
# Show our result
plt.title('Distances Measured in Step 3')
plt.show()


