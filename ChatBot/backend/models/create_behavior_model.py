import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import LSTM, Dense # type: ignore

data = np.random.random((1000, 100, 1))
labels = np.random.randint(2, size=(1000, 1))

model = Sequential([
    LSTM(50, activation='relu', input_shape=(100, 1)),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(data, labels, epochs=10, batch_size=32)

model.save('behavior_model.h5')