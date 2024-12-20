# Task 1: User Overview Analysis

## Objective
The objective of this task is to perform an in-depth exploratory data analysis (EDA) on a telecom dataset. The analysis focuses on understanding user behavior, identifying trends, and providing insights that could be useful for the marketing team.

## Sub-tasks

### 1.1 User Overview Analysis
- Identify the top 10 handsets used by the customers.
- Identify the top 3 handset manufacturers.
- Identify the top 5 handsets for each of the top 3 handset manufacturers.
- Provide recommendations based on findings.

### 1.2 User Behavior Analysis
- Aggregate user data from different applications (e.g., Social Media, Google, Email, YouTube, Netflix, Gaming, etc.).
  - Calculate the number of sessions, session duration, download (DL) and upload (UL) data, and total data volume for each application.
- Clean and preprocess the dataset by handling missing values and outliers.
  - Fill missing values using the median.
  - Handle zero values in data columns by replacing them with NaN.
  - Drop columns with more than 50% missing data.

### 1.3 Exploratory Data Analysis (EDA)
- Perform univariate analysis using graphical and non-graphical techniques:
  - Histogram for numerical columns like 'Total DL (Bytes)'.
  - Boxplot for detecting outliers in 'Total UL (Bytes)'.
  - Compute descriptive statistics (mean, median, etc.) for the dataset.
  - Visualize data distribution and dispersion for each column.
  
### 1.4 Bivariate and Multivariate Analysis
- Explore relationships between variables like 'Total DL (Bytes)' and 'Total UL (Bytes)' using scatter plots.
- Compute correlation between relevant columns, such as:
  - Social Media data, Google data, Email data, YouTube data, Netflix data, Gaming data, and Other data.
  
### 1.5 Dimensionality Reduction
- Apply Principal Component Analysis (PCA) to reduce the dimensionality of the data and interpret the results.

## Data Preprocessing and Cleaning
- **Missing values**: All missing numeric values are replaced with the median of the respective columns.
- **Zero values**: Columns with download (DL) and upload (UL) data have zero values replaced by NaN.
- **Outliers**: Outliers are identified using boxplots, and appropriate actions are taken.
  
## Key Findings
- **Top Applications**: Users spend significant time on social media, YouTube, and gaming apps.
- **Data Usage Trends**: High download and upload data volumes are associated with entertainment applications like YouTube and Netflix.
- **Correlation**: A positive correlation was found between certain applications' data usage (e.g., Social Media and Gaming).

## Technology Stack
- **Python Libraries**: pandas, matplotlib, seaborn
- **Data Sources**: Telecom Call Detail Record (CDR) data, XDR (Data Sessions Detail Record)
  

