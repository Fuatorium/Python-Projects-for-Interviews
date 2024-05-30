import requests
import pandas as pd
from datetime import datetime, timedelta

def get_crypto_data(crypto_id, days=365):
    url = f'https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart'
    
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    params = {
        'vs_currency': 'usd',
        'days': days
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print(data) 
        if 'prices' in data:
            prices = data['prices']
            df = pd.DataFrame(prices, columns=['timestamp', 'price'])
            df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
            df.set_index('date', inplace=True)
            df.drop('timestamp', axis=1, inplace=True)
            return df
        else:
            raise KeyError("'prices' anahtarı API yanıtında bulunamadı.")
    else:
        print(f"API isteği başarısız oldu: {response.status_code}")
        print(response.text)  
        raise ConnectionError(f"API isteği başarısız oldu: {response.status_code}")


if __name__ == "__main__":
    try:
        df = get_crypto_data('bitcoin')
        print(df.head())
    except Exception as e:
        print(f"Hata: {e}")
