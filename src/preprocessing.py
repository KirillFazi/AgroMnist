import pandas as pd
from sklearn.model_selection import train_test_split


train_data = pd.read_csv('../data/raw/mnist_train.csv')
test_data = pd.read_csv('../data/raw/mnist_test.csv')

X_train = train_data.drop('label', axis=1)
y_train = train_data['label']

X_val, X_test, y_val, y_test = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

X_test = test_data.drop('label', axis=1)
y_test = test_data['label']

X_train.to_csv('../dagta/processed/X_train.csv', index=False)
y_train.to_csv('../data/processed/y_train.csv', index=False)

X_val.to_csv('../data/processed/X_val.csv', index=False)
y_val.to_csv('../data/processed/y_val.csv', index=False)

X_test.to_csv('../data/processed/X_test.csv', index=False)
y_test.to_csv('../data/processed/y_test.csv', index=False)
