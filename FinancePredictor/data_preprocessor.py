import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(df):
    df = df[['price']].copy()  
    df.dropna(inplace=True)
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(df)
    return scaled_data, scaler


if __name__ == "__main__":
    from data_collector import get_crypto_data
    df = get_crypto_data('bitcoin')
    print(df.head())  
    scaled_data, scaler = preprocess_data(df)
    print(scaled_data[:5])  
