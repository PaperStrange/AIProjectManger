# Note 2019/3/2: use sklearn pipline foolwed the instruction from Udacity

from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin



X_train, y_train, X_test, y_test = [], [], [], []

pipline = Pipeline([
    ("name", "a transformation"),
    ("name", "a classifier or a transfomation")
])

pipline.fit(X_train)
y_pred = pipline.predict(X_test)
