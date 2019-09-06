import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs

# Generate data
data, labels = make_blobs(n_samples=120, centers=3, random_state=42)

# Create some centroids
centroids = np.array([[-5,-5], [0,0], [5,5]])

# Plot the data with centroids on top
plt.title('Data with Centroids')
plt.scatter(data[:,0], data[:,1])
plt.scatter(centroids[:,0], centroids[:,1], marker="x", color="red")
plt.show()
