# import joblib
# import sklearn
# print(sklearn.__version__)

# model = joblib.load(f"model.pkl")

import sklearn.compose._column_transformer as ct
print(hasattr(ct, "_RemainderColsList"))