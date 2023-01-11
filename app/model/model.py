import pickle
from pathlib import Path
import sklearn

__version__ = "0.2.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent

#model File.
file = open(f"{BASE_DIR}/trained_model-{__version__}.pkl","rb")

#Count Vectorizer File.
file2 = open(f"{BASE_DIR}/transform-{__version__}.pkl","rb")

model = pickle.load(file)
cv = pickle.load(file2)


# Function to predict the input.

def predict_pipeline(text):
    data = cv.transform([text]).toarray()
    output = model.predict(data)
    return output[0]
