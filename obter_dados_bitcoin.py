import requests
import pandas as pd
from datetime import datetime

# Definir a URL da API do CoinGecko para obter dados históricos de preços
url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"

# Definir o período (30 dias)
params = {
    'vs_currency': 'usd',
    'days': '120',
    'interval': 'daily'
}

# Fazer a requisição para a API
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    prices = data['prices']
    dates = [datetime.fromtimestamp(price[0] / 1000).date() for price in prices]
    price_values = [price[1] for price in prices]

    # Criar um DataFrame
    df = pd.DataFrame({
        'Date': dates,
        'Price': price_values
    })

    # Salvar em um arquivo CSV
    df.to_csv('bitcoin_prices_last_30_days.csv', index=False)

    print("CSV gerado com sucesso: bitcoin_prices_last_30_days.csv")
else:
    print("Erro ao obter dados da API:", response.status_code)
