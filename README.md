# Customer Engagement and Experience Analysis Project

This project focuses on analyzing customer engagement and experience, calculating satisfaction scores, and visualizing the results through interactive dashboards. The tasks cover data preprocessing, clustering, scoring, and visualization.

## Table of Contents
1. [Task 1: Data Preprocessing and Feature Engineering](#task-1-data-preprocessing-and-feature-engineering)
2. [Task 2: Clustering Analysis (Engagement and Experience)](#task-2-clustering-analysis-engagement-and-experience)
3. [Task 3: Assigning Engagement and Experience Scores](#task-3-assigning-engagement-and-experience-scores)
4. [Task 4: Satisfaction Score and Clustering](#task-4-satisfaction-score-and-clustering)
5. [Task 5: Dashboard Development](#task-5-dashboard-development)

---

## Task 1: Data Preprocessing and Feature Engineering

### Objective:
In this task, the goal is to clean the raw dataset and transform it into a format that can be used for analysis and modeling.

### Steps:
1. **Load Data**: Import the dataset into a pandas DataFrame.
2. **Handle Missing Values**: Check for missing data and either drop or impute the missing values.
3. **Feature Transformation**: Convert categorical features to numerical features, if necessary.
4. **Outlier Detection**: Detect and handle any outliers in the dataset.
5. **Feature Scaling**: Normalize or standardize features for consistency.

### How to Run:
1. Ensure the dataset is available.
2. Run the script to preprocess the data.
3. The cleaned dataset is ready for further tasks.

---

## Task 2: Clustering Analysis (Engagement and Experience)

### Objective:
In this task, we perform clustering on the data to categorize users based on their engagement and experience metrics using K-Means clustering.

### Steps:
1. **Select Features**: Choose relevant features for engagement and experience.
2. **K-Means Clustering**: Apply K-Means clustering to segment users.
3. **Analyze Clusters**: Interpret and understand the resulting clusters.
4. **Assign Cluster Labels**: Assign users to specific clusters based on their engagement and experience.

### How to Run:
1. Ensure that the preprocessed data from Task 1 is available.
2. Run the script to apply clustering to the data.
3. The result will include cluster labels for each user.

---

## Task 3: Assigning Engagement and Experience Scores

### Objective:
In this task, we calculate engagement and experience scores for each user by computing Euclidean distances to the respective cluster centroids.

### Steps:
1. **Calculate Engagement Score**: Compute the distance between user data and the "least engaged" cluster centroid.
2. **Calculate Experience Score**: Compute the distance between user data and the "worst experience" cluster centroid.
3. **Add Scores to Data**: Append engagement and experience scores to the dataset.

### How to Run:
1. Ensure that clustering results from Task 2 are available.
2. Run the script to calculate engagement and experience scores.
3. The resulting dataset will now include the calculated scores.

---

## Task 4: Satisfaction Score and Clustering

### Objective:
This task involves calculating a satisfaction score as the average of engagement and experience scores, followed by applying K-Means clustering to the satisfaction scores.

### Steps:
1. **Calculate Satisfaction Score**: Average the engagement and experience scores for each user.
2. **K-Means Clustering on Satisfaction Scores**: Apply K-Means clustering to the satisfaction scores.
3. **Assign Satisfaction Clusters**: Group users into satisfaction clusters.
4. **Cluster Aggregation**: Aggregate the satisfaction and experience scores for each cluster.

### How to Run:
1. Ensure the engagement and experience scores from Task 3 are available.
2. Run the script to compute the satisfaction scores and perform clustering.
3. The result will include satisfaction clusters and aggregated scores.

---

## Task 5: Dashboard Development

### Objective:
In this task, we create an interactive dashboard to visualize user engagement, experience, and satisfaction analysis using a visualization tool.

### Steps:
1. **Design the Dashboard**: Create separate pages for each analysis: User Overview, Engagement, Experience, and Satisfaction.
2. **Visualize Data**: Use Plotly to create interactive charts for each analysis:
   - User Overview: Visualize the distribution of users by cluster.
   - Engagement Analysis: Display the distribution of engagement scores.
   - Experience Analysis: Show the distribution of experience scores.
   - Satisfaction Analysis: Visualize the satisfaction score distribution.
3. **Deploy the Dashboard**: Host the dashboard on a platform like Heroku or PythonAnywhere for public access.

### How to Run:
1. Install necessary libraries:
   ```bash
   pip install dash plotly pandas
