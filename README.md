# Telecom User Analyzer

This project analyzes telecom data to derive insights about user engagement, session frequency, and traffic usage across different applications. It employs machine learning clustering techniques to categorize users based on their interaction patterns and generates useful statistics like session frequency, duration, and total traffic for analysis.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset Information](#dataset-information)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Analysis Steps](#analysis-steps)
- [Visualizations](#visualizations)
- [Contact Information](#contact-information)

## Project Overview

The Telecom User Analyzer uses clustering techniques to group users based on their telecom usage patterns. It processes raw telecom data to:

1. Calculate session frequency and duration for each user.
2. Apply K-Means clustering to identify patterns.
3. Analyze user traffic usage across different categories like social media, Google, YouTube, Netflix, etc.
4. Visualize user behavior and traffic distribution.

## Dataset Information

The dataset contains telecom usage data with the following key columns:
- **MSISDN/Number**: User's phone number.
- **Start**: Start time of the session.
- **End**: End time of the session.
- **Dur. (ms)**: Session duration in milliseconds.
- **Total UL (Bytes)**: Total uplink traffic in bytes.
- **Total DL (Bytes)**: Total downlink traffic in bytes.
- **Social Media DL (Bytes)**, **Social Media UL (Bytes)**: Traffic data for social media apps.
- **Google DL (Bytes)**, **Google UL (Bytes)**: Traffic data for Google apps.
- **Youtube DL (Bytes)**, **Youtube UL (Bytes)**: Traffic data for YouTube.

### The main objective is to understand how users interact with the telecom services and their preferences across various applications.

## Requirements

To run this project, you'll need the following Python libraries:
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

You can install these dependencies using pip:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

## How to Run

1. Clone the repository:

```bash
git clone <repository-url>
cd Telecom-User-Analyzer
```

2. Place your CSV dataset file in the `data/` directory.

3. Run the Python script to analyze the data:

```bash
python telecom_analyzer.py
```

This will generate the analysis, clustering results, and visualizations.

## Analysis Steps

### Step 1: Data Cleaning and Preprocessing

The data is first cleaned and preprocessed:
- Column names are standardized.
- If the **Dur. (ms)** column is missing, the script calculates the session duration using the **Start** and **End** timestamps.
  
### Step 2: User Engagement Metrics

The analysis generates several metrics for each user:
- **Session Frequency**: The number of sessions for each user.
- **Total Duration**: Total session duration for each user.
- **Total Traffic**: Sum of uplink and downlink traffic for each user.

### Step 3: Data Normalization

The session frequency, session duration, and total traffic are normalized using Min-Max scaling to ensure that all features contribute equally to the clustering process.

### Step 4: K-Means Clustering

The K-Means clustering algorithm is applied to categorize users into clusters based on their usage patterns. The ideal number of clusters (k) is determined using the **Elbow Method**.

### Step 5: Cluster Analysis

Once the clusters are formed, the analysis calculates:
- Minimum, maximum, average, and total session frequencies and durations for each cluster.
- Traffic analysis across various applications such as social media, Google, YouTube, etc.

### Step 6: Application Traffic Breakdown

Traffic usage is analyzed across different applications:
- Social Media (e.g., Facebook, Instagram)
- Google (e.g., Google Search, Google Maps)
- YouTube
- Netflix
- Gaming

### Step 7: Visualizations

Several plots and visualizations are generated to better understand the results:
- **K-Means Clusters**: A scatter plot showing users grouped into clusters based on session frequency and duration.
- **Top 3 Most Used Applications**: A bar plot showing the most popular applications based on traffic usage.
- **Elbow Method**: A plot showing the optimal number of clusters using the within-cluster sum of squares (WCSS).

## Visualizations

Here are the types of visualizations generated:

1. **User Engagement Clusters**: A scatter plot showing how users are grouped based on session frequency and total session duration.

   ![Cluster Visualization](images/cluster_plot.png)

2. **Top 3 Most Used Applications**: A bar chart showing which applications consume the most traffic.

   ![Application Traffic](images/top_apps.png)

3. **Elbow Method**: A plot that helps determine the ideal number of clusters for K-Means.

   ![Elbow Method](images/elbow_plot.png)

