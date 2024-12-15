### using XGBoost model with SHAP

import numpy as np
import pandas as pd
import xgboost as xgb

import shap

from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# Xndarray of shape (n_samples, n_features): The generated samples.
# yndarray of shape (n_samples,): The integer labels for class membership of each sample.

X, y = make_classification(n_samples=100, n_features=5, n_informative=3, random_state=0)
feature_names = ["x" + str(i + 1) for i in range(0, 5)]
data = pd.DataFrame(X, columns=feature_names)
data["target"] = y

X_train, X_test, y_train, y_test = train_test_split(
    data[feature_names], data.target, test_size=0.30, random_state=0  ## predictors only
)

### create and fit model
estimator = xgb.XGBClassifier()
estimator.fit(X_train, y_train)


def xgb_predict_proba(data_asarray):
    # print("data_asarray: ", data_asarray)
    data_asframe = pd.DataFrame(data_asarray, columns=feature_names)
    # print("estimator: ", estimator)
    # print("data_asframe: ", data_asframe)
    return estimator.predict_proba(data_asframe)


#### Kernel SHAP
X_summary = shap.kmeans(X_train, 10)
explainer = shap.KernelExplainer(xgb_predict_proba, X_summary)

## shapely values with kernel SHAP
shap_values_single = explainer.shap_values(X_test.iloc[[5]])
shap_obj = explainer(X_test, l1_reg="num_features(10)")
# print(shap_obj)
# shap.force_plot(shap_kernel_explainer.expected_value, shap_kernel_explainer.shap_values)
# print(shap_obj[:,:,1])
shap.plots.beeswarm(shap_obj[:, :, 1], show=False)
