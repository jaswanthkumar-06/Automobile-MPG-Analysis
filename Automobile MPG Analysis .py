
# 1. Import all necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for seaborn plots
sns.set_style("darkgrid")
# Set a larger default figure size for better visibility
plt.rcParams['figure.figsize'] = (10, 6)

## --- 2. Data Loading ---
print("--- 2. Data Loading & Initial Inspection ---")

# Load the MPG dataset directly from Seaborn for convenience
try:
    df = sns.load_dataset('mpg')
except ValueError:
    print("Could not load the MPG dataset from Seaborn. Please ensure Seaborn is installed.")
    exit()

print(f"Dataset loaded with {len(df)} rows and {len(df.columns)} columns.")
print("\nData Info:")
df.info()

## --- 3. Data Preprocessing (Pandas & NumPy) ---
print("\n--- 3. Data Cleaning and Feature Creation ---")

# a) Handle Missing Values (Horsepower)
# The 'horsepower' column has some missing values; we'll fill them with the median.
# Use NumPy's median calculation within Pandas:
hp_median = np.median(df['horsepower'].dropna())
df['horsepower'].fillna(hp_median, inplace=True)
print(f"Missing horsepower values filled with the median: {hp_median:.2f}")

# b) Create a Categorical Feature (Weight Category)
# Use NumPy's digitize to assign numerical values to bins, then map to categories.
weight_bins = [0, 2000, 3000, 4000, np.inf]
weight_labels = ['Light', 'Medium', 'Heavy', 'Very Heavy']
df['weight_category'] = pd.cut(df['weight'], bins=weight_bins, labels=weight_labels, right=False)

# c) Drop columns not needed for analysis (e.g., 'name')
df.drop('name', axis=1, inplace=True)

print("\nData after cleaning and feature creation:")
print(df.head())

## --- 4. Exploratory Data Analysis (Visualization) ---
print("\n--- 4. Exploratory Data Analysis & Visualization ---")

# A. Distribution of MPG (Matplotlib Histogram and Seaborn KDE)
plt.figure(figsize=(10, 6))
# Seaborn Histplot provides both the histogram and the smooth KDE line
sns.histplot(df['mpg'], bins=15, kde=True, color='teal', edgecolor='black')
plt.title('A. Distribution of Miles Per Gallon (MPG)')
plt.xlabel('MPG (Miles Per Gallon)')
plt.ylabel('Frequency')
plt.show()

# B. MPG vs. Weight (Seaborn Scatter Plot)
plt.figure(figsize=(10, 6))
# Use 'origin' as the hue to see the effect of country of origin
sns.scatterplot(
    x='weight', 
    y='mpg', 
    hue='origin', 
    size='horsepower', # Use horsepower to adjust the size of the marker
    data=df, 
    palette='magma', 
    sizes=(20, 300)
)
plt.title('B. MPG vs. Vehicle Weight, Colored by Origin')
plt.xlabel('Weight (lbs)')
plt.ylabel('MPG')
plt.legend(title='Origin', loc='upper right')
plt.show()

# C. MPG Distribution by Country of Origin (Seaborn Box Plot)
plt.figure(figsize=(8, 6))
sns.boxplot(x='origin', y='mpg', data=df, palette='viridis')
plt.title('C. MPG Distribution by Country of Origin')
plt.xlabel('Country of Origin')
plt.ylabel('MPG')
plt.show()

# D. Pairwise Relationship (Seaborn PairPlot - focuses on key numerical columns)
# This plot generates a grid of scatter plots for all numerical combinations,
# and histograms/KDEs on the diagonal. It is a powerful EDA tool.
numerical_cols = ['mpg', 'displacement', 'horsepower', 'weight']
sns.pairplot(df[numerical_cols], diag_kind='kde')
plt.suptitle('D. Pairwise Relationships (MPG, Displacement, Horsepower, Weight)', y=1.02)
plt.show()

# E. MPG of Cylinders (Pandas Groupby & Matplotlib Bar Chart)
# Use Pandas to calculate the mean MPG for each cylinder count
avg_mpg_by_cyl = df.groupby('cylinders')['mpg'].mean().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
avg_mpg_by_cyl.plot(kind='bar', color=plt.cm.coolwarm(np.linspace(0, 1, len(avg_mpg_by_cyl))))
plt.title('E. Average MPG by Number of Cylinders')
plt.xlabel('Number of Cylinders')
plt.ylabel('Average MPG')
plt.xticks(rotation=0)
plt.show()

## --- 5. Key Findings (Derived from Pandas & NumPy) ---
print("\n--- 5. Key Numerical Findings ---")

# Pandas Groupby for aggregated statistics
stats_by_origin = df.groupby('origin')['mpg'].agg(['mean', 'median', 'std', np.min, np.max])
print("MPG Statistical Summary by Country of Origin (Pandas):\n", stats_by_origin.to_string())