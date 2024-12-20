import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data_file = '/workspaces/Telecom-User-Analyzer/data/Copy of Week2_challenge_data_source(CSV).csv'
df = pd.read_csv(data_file)

# Display the first few rows to understand the structure of the dataset
print("First few rows of the dataset:")
print(df.head())

# Check for missing values
missing_values = df.isnull().sum()
print("\nMissing values per column:")
print(missing_values)

# Visualize missing data with seaborn heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap")
plt.show()

# Handling Missing Values
# Select only numeric columns to calculate the mean and fill missing values
numeric_cols = df.select_dtypes(include=['number']).columns

# Fill missing values with the median (optional: you can use mean instead depending on your data)
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

# Replace zero values in specific columns with NaN
columns_with_zeros = ['Social Media DL (Bytes)', 'Google DL (Bytes)', 'Email DL (Bytes)', 'Youtube DL (Bytes)', 'Netflix DL (Bytes)', 'Gaming DL (Bytes)', 'Other DL (Bytes)']
df[columns_with_zeros] = df[columns_with_zeros].replace(0, pd.NA)

# Handling columns with too many missing values by dropping them
threshold = 0.5  # 50% missing data threshold
df = df.dropna(thresh=int((1 - threshold) * len(df)), axis=1)

# Data Conversion (Convert 'Start' and 'End' columns to datetime format)
if 'Start' in df.columns and 'End' in df.columns:
    df['Start'] = pd.to_datetime(df['Start'], errors='coerce')
    df['End'] = pd.to_datetime(df['End'], errors='coerce')
    # Forward fill missing datetime data (if necessary)
    df['Start'] = df['Start'].fillna(method='ffill')
    df['End'] = df['End'].fillna(method='ffill')
    print("\nData types after conversion:")
    print(df.dtypes)
else:
    print("\n'Empty' or 'Start'/'End' columns not found in the dataset.")

# Visualizing the Data
# Plot histogram for 'Total DL (Bytes)'
plt.figure(figsize=(10, 6))
sns.histplot(df['Total DL (Bytes)'], bins=50, kde=True)
plt.title('Histogram of Total DL (Bytes)')
plt.show()

# Plot boxplot for 'Total UL (Bytes)'
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Total UL (Bytes)'])
plt.title('Boxplot of Total UL (Bytes)')
plt.show()

# Grouping by Bearer Id to summarize data usage
user_summary = df.groupby('Bearer Id').agg({
    'Total DL (Bytes)': 'sum',
    'Total UL (Bytes)': 'sum',
    'Avg RTT DL (ms)': 'mean',
    'Avg RTT UL (ms)': 'mean'
}).reset_index()

print("\nUser Summary based on Bearer Id:")
print(user_summary.head())

# Check the basic statistics of the dataset
print("\nDescriptive Statistics:")
print(df.describe())

# Optional: Check the data types to ensure correctness
print("\nData Types:")
print(df.dtypes)

# Explore relationships between network metrics and data usage
# Calculate the correlation matrix between relevant columns
correlation_matrix = df[['Avg RTT DL (ms)', 'Avg RTT UL (ms)', 'Avg Bearer TP DL (kbps)', 'Avg Bearer TP UL (kbps)', 'Total DL (Bytes)', 'Total UL (Bytes)']].corr()

print("\nCorrelation Matrix:")
print(correlation_matrix)

# Visualizing the Correlation Matrix with a Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix between Network Metrics and Data Usage')
plt.show()

# Scatter plot for Avg RTT DL (ms) vs Total DL (Bytes)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Avg RTT DL (ms)', y='Total DL (Bytes)', data=df)
plt.title('Avg RTT DL (ms) vs Total DL (Bytes)')
plt.show()

# Scatter plot for Avg Bearer TP DL (bps) vs Total UL (Bytes)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Avg Bearer TP DL (bps)', y='Total UL (Bytes)', data=df)
plt.title('Avg Bearer TP DL (bps) vs Total UL (Bytes)')
plt.show()

# Pairplot to see relationships between multiple columns
sns.pairplot(df[['Avg RTT DL (ms)', 'Avg RTT UL (ms)', 'Avg Bearer TP DL (bps)', 'Total DL (Bytes)', 'Total UL (Bytes)']])
plt.show()

