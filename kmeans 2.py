import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Gerar dados de exemplo
X = np.array([[1, 2], [5, 8], [1.5, 1.8], [8, 8], [1, 0.6], [9, 11]])

# Criar o objeto KMeans com 2 clusters
kmeans = KMeans(n_clusters=2)

# Treinar o modelo
kmeans.fit(X)

# Obter os centróides dos clusters
centroids = kmeans.cluster_centers_

# Obter os rótulos dos clusters para cada ponto
labels = kmeans.labels_

# Plotar os pontos e os centróides
plt.scatter(X[:,0], X[:,1], c=labels, cmap='viridis', marker='o')
plt.scatter(centroids[:,0], centroids[:,1], c='red', marker='x', s=200)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('K-Means Clustering')
plt.show()

predicted = kmeans.predict([[1,2],[1.5,1.8]])
print(predicted)

