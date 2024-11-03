from sklearn.tree import DecisionTreeClassifier

# Dados de exemplo
X = [[0, 0], [1, 1]]
y = [0, 1]

# Treinamento do modelo
model = DecisionTreeClassifier().fit(X, y)

# Predição
predicted = model.predict([[2, 2]])
print(predicted)

