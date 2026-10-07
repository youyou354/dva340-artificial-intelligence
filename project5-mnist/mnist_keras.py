import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras

#Made by EL OTMANI Youssef

#load
path = "C:\\Users\\elotm\\Downloads\\assignment5.csv"  #?
data = pd.read_csv(path)

#seperate the first column (label) from the other columns
X = data.iloc[:, 1:].values  
y = data.iloc[:, 0].values 

#transforming values between 0 & 255 to a proportional value between 0 & 1 representing probabillity
X = X / 255 

# Seperation the data 
total_samples = X.shape[0]
train_size = int(0.7 * total_samples) #70%
val_size = int(0.1 * total_samples) #10 %
test_size = total_samples - train_size - val_size  # 20%
X_train, y_train = X[:train_size], y[:train_size]
X_verif, y_verif = X[train_size:train_size + val_size], y[train_size:train_size + val_size]
X_test, y_test = X[train_size + val_size:], y[train_size + val_size:]

#one-hot encod
y_train = keras.utils.to_categorical(y_train, num_classes=10) #10 because 10 different numbers possible
y_verif = keras.utils.to_categorical(y_verif, num_classes=10)
y_test = keras.utils.to_categorical(y_test, num_classes=10)

print("\ntrain set :", X_train.shape, y_train.shape)
print("validation set :", X_verif.shape, y_verif.shape)
print("test set :", X_test.shape, y_test.shape, "\n")


model = keras.Sequential ((
    keras.layers.Dense(128, input_shape=(784,), activation='relu'),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(10, activation='softmax'), #proba
))


model.compile(
    optimizer='sgd', #opti  weight
    loss='categorical_crossentropy',
    metrics=['accuracy'] 
)

print("\ntraining session")
model.fit(X_train, y_train, epochs=5, validation_data=(X_verif, y_verif))

print("\ntest")
model.evaluate(X_test, y_test)
