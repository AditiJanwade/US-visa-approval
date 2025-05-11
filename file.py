import joblib
import sklearn
print(sklearn.__version__)

model = joblib.load(f"model.pkl")
