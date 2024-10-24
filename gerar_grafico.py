import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do arquivo CSV
dados = pd.read_csv('bitcoin_prices_last_30_days.csv')

# Converter a coluna de data para o tipo datetime
dados['date'] = pd.to_datetime(dados['date'])

# Plotar o gráfico
plt.figure(figsize=(12, 6))
plt.plot(dados['date'], dados['price'], marker='o', linestyle='-', color='blue')

# Adicionar título e rótulos aos eixos
plt.title('Preço do Bitcoin nos Últimos 30 Dias', fontsize=14)
plt.xlabel('Data', fontsize=12)
plt.ylabel('Preço (USD)', fontsize=12)
plt.grid()

# Exibir o gráfico
plt.xticks(rotation=45)  # Rotaciona as datas para melhor visualização
plt.tight_layout()        # Ajusta o layout para evitar sobreposição
plt.show()
