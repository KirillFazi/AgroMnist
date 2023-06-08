import pandas as pd
from sklearn.model_selection import train_test_split
import sys
import random
import os

import yaml

params = yaml.safe_load(open("params.yaml"))["preprocess"]

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython preprocess.py data-file\n")
    sys.exit(1)

split = params["split"]
random_seed = params["seed"]

input_dir = os.path.join("data", "raw")

output_dir = os.path.join("data", "processed")
os.makedirs(output_dir, exist_ok=True)

train_data = pd.read_csv(os.path.join(input_dir, "mnist_train.csv"))
test_data = pd.read_csv(os.path.join(input_dir, "mnist_test.csv"))

X_train = train_data.drop('label', axis=1)
y_train = train_data['label']

X_train, X_val, y_train, y_val = train_test_split(
    X_train, y_train,
    test_size=split,
    random_state=random_seed,
    stratify=y_train)

X_test = test_data.drop('label', axis=1)
y_test = test_data['label']

X_train.to_csv(os.path.join(output_dir, "X_train.csv"), index=False)
y_train.to_csv(os.path.join(output_dir, "y_train.csv"), index=False)

X_val.to_csv(os.path.join(output_dir, "X_val.csv"), index=False)
y_val.to_csv(os.path.join(output_dir, "y_val.csv"), index=False)

X_test.to_csv(os.path.join(output_dir, "X_test.csv"), index=False)
y_test.to_csv(os.path.join(output_dir, "y_test.csv"), index=False)


"""
dvc stage add -n prepare \
                -p prepare.seed,prepare.split \
                -d src/prepare.py -d data/data.xml \
                -o data/prepared \
                python src/prepare.py data/data.xml
"""