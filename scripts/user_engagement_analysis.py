
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

# Load the dataset (assuming it's already loaded as 'df')
data_file = '/workspaces/Telecom-User-Analyzer/data/Copy of Week2_challenge_data_source(CSV).csv'
df = pd.read_csv(data_file)

# Print column names to check for any typos or unexpected names
print(df.columns)

# Clean up column names by stripping any leading/trailing whitespaces
df.columns = df.columns.str.strip()

# Check the first few rows of the dataframe
print(df.head())

# Check if 'Session Duration' column exists, if not, calculate it using 'Start' and 'End' columns
if 'Dur. (ms)' not in df.columns:
    print("Dur. (ms) column not found. Attempting to calculate session duration.")
    # Ensure 'Start' and 'End' columns are in datetime format
    df['Start'] = pd.to_datetime(df['Start'], errors='coerce')
    df['End'] = pd.to_datetime(df['End'], errors='coerce')

    # Now, calculate the session duration in milliseconds
    df['Dur. (ms)'] = (df['End'] - df['Start']).dt.total_seconds() * 1000  # converting to milliseconds

# Calculate session frequency by counting the number of sessions per MSISDN/Number
session_freq = df.groupby('MSISDN/Number')['Dur. (ms)'].count().reset_index(name='Session Frequency')
print(session_freq)

# Grouping by MSISDN/Number to calculate the engagement metrics
metrics = df.groupby('MSISDN/Number').agg(
    session_frequency=('Dur. (ms)', 'count'),
    total_duration=('Dur. (ms)', 'sum'),
    total_traffic=('Total UL (Bytes)', 'sum') + ('Total DL (Bytes)', 'sum')
).reset_index()

# Display the calculated metrics
print(metrics.head())

# Normalize the metrics using Min-Max Scaling
scaler = MinMaxScaler()
metrics[['session_frequency', 'total_duration', 'total_traffic']] = scaler.fit_transform(
    metrics[['session_frequency', 'total_duration', 'total_traffic']])

# Display the normalized metrics
print(metrics.head())

# Applying K-Means clustering (k=3)
kmeans = KMeans(n_clusters=3, random_state=42)
metrics['cluster'] = kmeans.fit_predict(metrics[['session_frequency', 'total_duration', 'total_traffic']])

# Display the clustered metrics
print(metrics.head())

# Calculate the minimum, maximum, average, and total of non-normalized metrics for each cluster
cluster_analysis = df.groupby('cluster').agg(
    min_session_freq=('Dur. (ms)', 'count'),
    max_session_freq=('Dur. (ms)', 'count'),
    avg_session_freq=('Dur. (ms)', 'mean'),
    total_session_freq=('Dur. (ms)', 'sum'),
    min_duration=('Dur. (ms)', 'sum'),
    max_duration=('Dur. (ms)', 'sum'),
    avg_duration=('Dur. (ms)', 'mean'),
    total_duration=('Dur. (ms)', 'sum'),
    min_traffic=('Total UL (Bytes)', 'sum') + ('Total DL (Bytes)', 'sum'),
    max_traffic=('Total UL (Bytes)', 'sum') + ('Total DL (Bytes)', 'sum'),
    avg_traffic=('Total UL (Bytes)', 'mean') + ('Total DL (Bytes)', 'mean'),
    total_traffic=('Total UL (Bytes)', 'sum') + ('Total DL (Bytes)', 'sum')
).reset_index()

# Display the cluster analysis
print(cluster_analysis)

# Aggregating traffic per application (for example: Social Media, Google, Youtube, etc.)
application_traffic = df.groupby('MSISDN/Number').agg(
    social_media_traffic=('Social Media DL (Bytes)', 'sum') + ('Social Media UL (Bytes)', 'sum'),
    google_traffic=('Google DL (Bytes)', 'sum') + ('Google UL (Bytes)', 'sum'),
    youtube_traffic=('Youtube DL (Bytes)', 'sum') + ('Youtube UL (Bytes)', 'sum'),
    netflix_traffic=('Netflix DL (Bytes)', 'sum') + ('Netflix UL (Bytes)', 'sum'),
    gaming_traffic=('Gaming DL (Bytes)', 'sum') + ('Gaming UL (Bytes)', 'sum')
).reset_index()

# Display the application traffic data
print(application_traffic.head())

# Visualize the KMeans clustering results
sns.scatterplot(data=metrics, x='session_frequency', y='total_duration', hue='cluster', palette='viridis')
plt.title('User Engagement Clusters')
plt.xlabel('Session Frequency')
plt.ylabel('Session Duration')
plt.show()

# Visualize the top 3 most used applications
top_apps = application_traffic[['social_media_traffic', 'google_traffic', 'youtube_traffic']].sum()
top_apps = top_apps.sort_values(ascending=False)

# Plot the top 3 applications
top_apps.plot(kind='bar', title='Top 3 Most Used Applications')
plt.ylabel('Traffic (Bytes)')
plt.show()

# Elbow Method for determining the optimal number of clusters
wcss = []
for i in range(1, 11):  # Testing for k=1 to k=10
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(metrics[['session_frequency', 'total_duration', 'total_traffic']])
    wcss.append(kmeans.inertia_)

# Plotting the Elbow Method
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method for Optimal K')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS (Within-cluster Sum of Squares)')
plt.show()

# Display data types of columns to check for any inconsistencies
print(df.dtypes)
