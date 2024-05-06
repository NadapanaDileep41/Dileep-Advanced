import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error

# Load the California housing dataset
california_housing = fetch_california_housing(as_frame=True)
X = california_housing.data
y = california_housing.target

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)
print("Train Score:", train_score)
print("Test Score:", test_score)

# Predictions
train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)

# Plot residuals
plt.figure(figsize=(10, 6))
plt.scatter(train_predictions, train_predictions - y_train, c='b', s=40, alpha=0.5, label='Train')
plt.scatter(test_predictions, test_predictions - y_test, c='g', s=40, label='Test')
plt.hlines(y=0, xmin=0, xmax=5)
plt.title('Residual Plot')
plt.ylabel('Residuals')
plt.legend()
plt.show()
