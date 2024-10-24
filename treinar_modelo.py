import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Carregar os dados pré-processados
X = pd.read_csv('features.csv')
y = pd.read_csv('target.csv').values.ravel()  # Transformar em array 1D

# Dividir os dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar e treinar o modelo
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Fazer previsões
y_pred = model.predict(X_test)

# Avaliar o modelo
print(classification_report(y_test, y_pred))
print("Acurácia:", accuracy_score(y_test, y_pred))

# Salvar o modelo treinado
import joblib
joblib.dump(model, 'modelo_bitcoin.pkl')
print("Modelo treinado e salvo com sucesso.")
