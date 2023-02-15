import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM

# Load historical stock price data from CSV file
df = pd.read_csv('stock_prices.csv')

# Create a new dataframe with just the 'Close' column
data = df.filter(['Close'])

# Convert the data to a numpy array
dataset = data.values

# Scale the data to values between 0 and 1
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(dataset)

# Define the number of time steps to use in the LSTM model
time_steps = 60

# Create the training dataset
train_data = scaled_data[:int(len(dataset) * 0.8)]
x_train = []
y_train = []

for i in range(time_steps, len(train_data)):
    x_train.append(train_data[i - time_steps:i, 0])
    y_train.append(train_data[i, 0])

x_train, y_train = np.array(x_train), np.array(y_train)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

# Define the LSTM model
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(x_train, y_train, batch_size=1, epochs=1)

# Create the testing dataset
test_data = scaled_data[int(len(dataset) * 0.8) - time_steps:]
x_test = []
y_test = dataset[int(len(dataset) * 0.8):]

for i in range(time_steps, len(test_data)):
    x_test.append(test_data[i - time_steps:i, 0])

x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

# Use the model to make predictions
predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)

# Plot the actual stock prices and the predicted prices
plt.plot(y_test)
plt.plot(predictions)
plt.show()
