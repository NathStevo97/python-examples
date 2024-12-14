import xgboost
import shap
import numpy as np

# train XGBoost model
X, y = shap.datasets.adult()
model = xgboost.XGBClassifier().fit(X, y)

# compute SHAP values
explainer = shap.TreeExplainer(model, X)
shap_values = explainer(X)
shap.plots.beeswarm(shap_values)