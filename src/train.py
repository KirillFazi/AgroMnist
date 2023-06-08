import os
import pandas as pd

import yaml

from keras.models import Sequential
from keras.layers import Dense, GlobalAveragePooling2D, Dropout
from keras.optimizers import Adam
from keras.utils import to_categorical

params = yaml.safe_load(open("params.yaml"))["train"]

epochs = params["epochs"]
batch_size = params["batch_size"]
lr = params["lr"]
num_classes = params["num_classes"]

input_dir = os.path.join("data", "processed")

X_train = pd.read_csv(os.path.join(input_dir, "X_train.csv"))
y_train = pd.read_csv(os.path.join(input_dir, "y_train.csv"))

y_train = to_categorical(y_train, num_classes=num_classes)

X_val = pd.read_csv(os.path.join(input_dir, "X_val.csv"))
y_val = pd.read_csv(os.path.join(input_dir, "y_val.csv"))

y_val = to_categorical(y_val, num_classes=num_classes)

model = Sequential()

model.add(Dense(512, activation='relu', input_shape=X_train.shape[1:]))
model.add(Dropout(0.2))
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(num_classes, activation='softmax'))

model.compile(
    loss='categorical_crossentropy',
    optimizer=Adam(lr=lr),
    metrics=['accuracy']
)

model.fit(
    X_train,
    y_train,
    epochs=epochs,
    batch_size=batch_size,
    validation_data=(X_val, y_val)
)

os.makedirs("models", exist_ok=True)
model.save(os.path.join("models", "model.h5"))



