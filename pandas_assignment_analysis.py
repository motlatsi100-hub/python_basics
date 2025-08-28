# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 11:41:17 2025

@author: motlatsi seeko
"""

# ===========================================
# Data Analysis and Visualization with Pandas & Matplotlib
# Author: Your Name
# ===========================================

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# -------------------------------
# Task 1: Load and Explore Dataset
# -------------------------------

try:
    # Option 1: Load from sklearn dataset (Iris)
    iris = load_iris(as_frame=True)
    df = iris.frame  # pandas DataFrame
    df['species'] = iris.target_names[iris.target]  # add species column

    # Option 2: Load from CSV (uncomment if you have a CSV file)
    # df = pd.read_csv("your_dataset.csv")

    print("Dataset loaded successfully!\n")
except FileNotFoundError:
    print("Error: CSV file not found. Please check the file path.")
    df = pd.DataFrame()  # empty fallback

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head(), "\n")

# Check data types and missing values
print("Dataset Info:")
print(df.info(), "\n")
print("Missing values per column:")
print(df.isnull().sum(), "\n")

# Clean dataset (no missing values in Iris, but example for others)
df = df.dropna()

# -------------------------------
# Task 2: Basic Data Analysis
# -------------------------------

# Basic statistics
print("Basic statistics of numerical columns:")
print(df.describe(), "\n")

# Grouping: mean of petal length per species
grouped = df.groupby("species")["petal length (cm)"].mean()
print("Average petal length per species:")
print(grouped, "\n")

# Observation
print("Observation: Iris-virginica tends to have the longest petals on average.\n")

# -------------------------------
# Task 3: Data Visualization
# -------------------------------

# 1. Line chart (trends) - Use sepal length over index (not time data, but demo)
plt.figure(figsize=(8, 5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length", color="blue")
plt.title("Line Chart of Sepal Lengths")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart - average petal length per species
plt.figure(figsize=(8, 5))
grouped.plot(kind="bar", color=["green", "orange", "purple"])
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram - distribution of sepal width
plt.figure(figsize=(8, 5))
plt.hist(df["sepal width (cm)"], bins=20, color="skyblue", edgecolor="black")
plt.title("Histogram of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot - sepal length vs. petal length
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="sepal length (cm)", y="petal length (cm)", hue="species")
plt.title("Scatter Plot of Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
