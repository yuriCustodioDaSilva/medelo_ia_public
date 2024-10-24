import pandas as pd
import joblib

# Carregar o modelo treinado
model = joblib.load('modelo_bitcoin.pkl')

# Exemplo de uso do modelo com novos dados
# Aqui, você deve calcular o preço atual e a variação
current_price = 30000  # Substitua pelo preço atual real
current_change = 0.01  # Substitua pela variação percentual real

# Criar um DataFrame com os dados atuais
new_data = pd.DataFrame({
    'Price': [current_price],
    'Price_Change': [current_change]
})

# Prever
prediction = model.predict(new_data)
if prediction[0] == 1:
    print("A previsão é que o Bitcoin suba.")
else:
    print("A previsão é que o Bitcoin desça.")
