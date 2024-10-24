import pandas as pd

# Carregar os dados do CSV
df = pd.read_csv('bitcoin_prices_last_30_days.csv')

# Calcular a variação percentual
df['Price_Change'] = df['Price'].pct_change()
df['Target'] = (df['Price_Change'] > 0).astype(int)

# Remover linhas com dados ausentes
df.dropna(inplace=True)

# Definir características e alvo
X = df[['Price', 'Price_Change']]
y = df['Target']

# Salvar X e y para uso posterior
X.to_csv('features.csv', index=False)
y.to_csv('target.csv', index=False)

print("Dados pré-processados e salvos com sucesso.")
