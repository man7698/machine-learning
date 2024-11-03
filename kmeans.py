from sklearn.cluster import KMeans

# Dados de exemplo
X = [[1], [2], [3], [8], [9], [10]]

# Treinamento do modelo
model = KMeans(n_clusters=6).fit(X)

# Predição
predicted = model.predict([[0],[4]])
print(predicted)


------------------------------------------