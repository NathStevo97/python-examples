import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the Dataset
df = pd.read_csv("../datasets/USA_Housing.csv")

# printing the dimensions of the dataframe
print(df.shape)

# Show first few rows of the dataset
print(df.head())

# Check for null / missing values
print(df.isnull().sum())

# data info
print(df.info())

# correlation
print(df.corr(numeric_only=True))

plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
# plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x="Avg. Area Income", y="Price", data=df)
# plt.show()

## Preprocessing

# Handle missing values if necessary
df.dropna(inplace=True)

# Split the data into features (X) and target variable (y)
X = df[["Avg. Area Income"]]
y = df["Price"]

# Split the data into training and testing sets (e.g., 80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Using precision score
model.score(X_test, y_test)

# Plot the regression line
plt.scatter(X_test, y_test, color="gray")
plt.plot(X_test, y_pred, color="red", linewidth=2)
plt.xlabel("Avg. Area Income")
plt.ylabel("Price")
plt.show()

print("MSE:", mean_squared_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
