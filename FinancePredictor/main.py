import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

warnings.filterwarnings("ignore", category=UserWarning, module="seaborn")
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")


from data_collector import get_crypto_data
from data_preprocessor import preprocess_data
from model import create_model, train_model
from predictor import predict, plot_predictions

def calculate_metrics(y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, y_pred)
    return mae, mse, rmse, r2

try:
    df = get_crypto_data('bitcoin')  
    scaled_data, scaler = preprocess_data(df)

    model = create_model()
    trained_model = train_model(model, scaled_data)

    predicted_price = predict(trained_model, scaled_data, scaler, future_days=1)
    future_prices = predict(trained_model, scaled_data, scaler, future_days=120)
    plot_predictions(df, predicted_price, future_prices)

    y_true = scaler.inverse_transform(scaled_data[-60:])  
    predicted_past = predict(trained_model, scaled_data[:-60], scaler, future_days=60)  
    mae, mse, rmse, r2 = calculate_metrics(y_true, predicted_past)
    print(f"MAE: {mae}")
    print(f"MSE: {mse}")
    print(f"RMSE: {rmse}")
    print(f"R²: {r2}")

except Exception as e:
    print(f"Hata: {e}")

mean_true_value = np.mean(y_true)

mean_absolute_error_rate = mae / mean_true_value * 100

accuracy_percentage = 100 - mean_absolute_error_rate

print(f"Ortalama Hata Oranı: %{mean_absolute_error_rate:.2f}")
print(f"Doğruluk Yüzdesi: %{accuracy_percentage:.2f}")