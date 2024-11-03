from sklearn.linear_model import LinearRegression

# Dados de exemplo
X = [[1], [2], [3]]
y = [2, 4, 6]

# Treinamento do modelo
model = LinearRegression().fit(X, y)

# Predição
predicted = model.predict([[10]])
print(predicted)

