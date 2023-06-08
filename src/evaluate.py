import os

import json
import yaml
import pandas as pd
import numpy as np

from keras.utils import to_categorical
from keras.models import load_model

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
params = yaml.safe_load(open('params.yaml'))['evaluate']

num_classes = params['num_classes']
metrics = params['metrics']

data_dir = os.path.join('data', 'processed')

X_test = pd.read_csv(os.path.join(data_dir, 'X_test.csv'))
y_test = pd.read_csv(os.path.join(data_dir, 'y_test.csv'))

y_test = to_categorical(y_test, num_classes=num_classes)

model = load_model(os.path.join('models', 'model.h5'))

y_pred = model.predict(X_test)

y_pred = np.argmax(y_pred, axis=1)
y_test = np.argmax(y_test, axis=1)

metrics_results = {
    'accuracy': accuracy_score(y_test, y_pred),
    'precision': precision_score(y_test, y_pred, average='macro'),
    'recall': recall_score(y_test, y_pred, average='macro'),
    'f1': f1_score(y_test, y_pred, average='macro')
}

os.makedirs('metrics', exist_ok=True)
with open(os.path.join('metrics', 'metrics.json'), 'w') as outfile:
    json.dump(metrics_results, outfile)



