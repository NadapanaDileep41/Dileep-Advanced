# Importing necessary libraries
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the Iris dataset from Seaborn
iris_df = sns.load_dataset('iris')

# Display the first few rows of the dataset
print("First few rows of the Iris dataset:")
print(iris_df.head())

# Basic information about the dataset
print("\nInfo about the Iris dataset:")
print(iris_df.info())

# Summary statistics of the numerical columns
print("\nSummary statistics of the Iris dataset:")
print(iris_df.describe())

# Check for any missing values
print("\nMissing values in the Iris dataset:")
print(iris_df.isnull().sum())

# Visualizing the distribution of each feature using histograms
iris_df.hist(figsize=(10, 8))
plt.suptitle('Distribution of Features in Iris Dataset')
plt.show()

# Visualizing the pairwise relationships between features
sns.pairplot(iris_df, hue='species', diag_kind='kde')
plt.suptitle('Pairwise Relationships in Iris Dataset')
plt.show()

# Correlation matrix heatmap
correlation_matrix = iris_df.drop(columns='species').corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Iris Dataset')
plt.show()
