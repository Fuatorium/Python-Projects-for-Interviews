import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def predict(model, data, scaler, future_days=30):
    last_60_days = data[-60:]
    x_test = np.array([last_60_days])
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    predicted_prices = []
    for _ in range(future_days):
        predicted_price = model.predict(x_test)
        predicted_prices.append(predicted_price[0, 0])
        x_test = np.append(x_test[:, 1:, :], np.reshape(predicted_price, (1, 1, 1)), axis=1)
    
    predicted_prices = scaler.inverse_transform(np.array(predicted_prices).reshape(-1, 1))
    return predicted_prices

def plot_predictions(df, predicted_price, future_prices):
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['price'], color='blue', label='Asıl fiyat')
    plt.plot(df.index[-1:], predicted_price, color='red', marker='o', markersize=5, label='Tahmini Fiyat')
    plt.title('Kripto Para Fiyat Tahmini')
    plt.xlabel('Zaman')
    plt.ylabel('Fiyat')
    plt.legend()
    plt.show()

    future_dates = pd.date_range(start=df.index[-1], periods=len(future_prices), inclusive='right')
    plt.figure(figsize=(10, 6))
    plt.plot(future_dates, future_prices.flatten()[:len(future_dates)], color='red', marker='o', markersize=5, label='Gelecek Tahmini Fiyat')
    plt.title('Kripto Para Fiyat Tahmini')
    plt.xlabel('Zaman')
    plt.ylabel('Fiyat')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    from model import create_model, train_model
    from data_collector import get_crypto_data
    from data_preprocessor import preprocess_data

    df = get_crypto_data('bitcoin')
    scaled_data, scaler = preprocess_data(df)
    model = create_model()
    trained_model = train_model(model, scaled_data)
    predicted_price = predict(trained_model, scaled_data, scaler, future_days=1)
    future_prices = predict(trained_model, scaled_data, scaler, future_days=120)
    plot_predictions(df, predicted_price, future_prices)
