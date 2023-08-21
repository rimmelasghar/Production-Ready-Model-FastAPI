import pickle
import re
from pathlib import Path
import pandas as pd

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent


with open(f"{BASE_DIR}/xgboost_model_pipeline-{__version__}.pkl", "rb") as file:
    model = pickle.load(file)

# classifcation classes
classes = [
    "Iris-setosa",
    "Iris-versicolor",
    "Iris-virginica",
]


def predict_pipeline(data):
    single_df = pd.DataFrame([data.dict()])
    single_pred = model.predict(single_df)
    return classes[single_pred[0]]
