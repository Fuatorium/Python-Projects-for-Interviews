import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

def create_model():
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(60, 1)))
    model.add(LSTM(units=50))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def train_model(model, train_data, epochs=10, batch_size=32):
    x_train, y_train = [], []
    for i in range(60, len(train_data)):
        x_train.append(train_data[i-60:i, 0])
        y_train.append(train_data[i, 0])
    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size)
    return model

if __name__ == "__main__":
    from data_collector import get_crypto_data
    from data_preprocessor import preprocess_data
    df = get_crypto_data('bitcoin', '2020-01-01', '2023-01-01')
    scaled_data, scaler = preprocess_data(df)
    model = create_model()
    trained_model = train_model(model, scaled_data)
