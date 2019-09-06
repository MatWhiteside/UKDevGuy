import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans

# Generate our data
data, labels = make_blobs(n_samples=120, centers=3, random_state=42)

# Run k-means with k=1..10 and record the sum of
# squared distances for each (denoted by inertia_)
x = []
ssd_list = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k).fit(data)
    cluster_labels = kmeans.predict(data)
    x.append(k)
    # kmeans.inertia_ represents SSD
    ssd_list.append(kmeans.inertia_)

# Plot our results into a line graph
plt.title("Sum of Squared Distances vs k")
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.xlabel("k")
plt.ylabel("Sum of Squared Distances")
plt.plot(x, ssd_list, 'o-')
plt.show()
