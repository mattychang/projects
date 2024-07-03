# Customer Segmentation Analysis
## Author: Matthew Chang

This project performs customer segmentation analysis on a dataset of mall customers using both KMeans and DBSCAN clustering algorithms. The analysis aims to identify different customer groups based on their annual income and spending score, allowing businesses to tailor their marketing strategies accordingly.

## Dataset
The dataset used for this analysis is `Mall_Customers.csv`, which contains the following columns:
- `CustomerID`: Unique ID assigned to the customer
- `Gender`: Gender of the customer
- `Age`: Age of the customer
- `Annual Income (k$)`: Annual income of the customer in thousands of dollars
- `Spending Score (1-100)`: Score assigned by the mall based on customer behavior and spending nature

## Requirements
- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

## Installation
1. Download the `Mall_Customers.csv` dataset and place it in the project directory.

2. Install the required libraries:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

## Usage
1. Ensure the `Mall_Customers.csv` file is in the project directory.
2. Run the Jupyter Notebook `customer_analytics.ipynb` to perform the analysis.

## Analysis Steps
The notebook performs the following steps:

1. ### Data Loading and Exploration:
   - Load the dataset and display the first few rows.
   - Visualize distributions and relationships of numerical variables.
   - Visualize gender distribution.

2. ### Data Preprocessing:
    - Select relevant features (`Annual Income (k$)` and `Spending Score (1-100)`) for clustering.
    - Standardize the features using StandardScaler.
    
3. ### KMeans Clustering:
    - Determine the optimal number of clusters using the elbow method.
    - Apply KMeans clustering with the chosen number of clusters.
    - Visualize the resulting clusters and their centers.
    - Calculate and display the mean values of `Age`, `Annual Income (k$)`, and `Spending Score (1-100)` for each cluster.

4. ### DBSCAN Clustering:
    - Apply the DBSCAN algorithm for clustering.
    - Identify and count the number of outliers.
    - Calculate and display the mean values of `Age`, `Annual Income (k$)`, and `Spending Score (1-100)` for each cluster, including outliers.
    - Visualize the resulting clusters and their centers.
    - Filter out the outliers and calculate the means of the filtered clusters.
    - Visualize the filtered clusters and their centers.

5. ### Cluster Evaluation:
    - Calculate and compare silhouette scores for both KMeans and DBSCAN (with outliers removed).

6. ### Additional Analysis:
    - Calculate and display the maximum values for each DBSCAN cluster.
    - Create age groups and add them to the dataframe.
    - Calculate the spending ratio and add it to the dataframe.
    - Identify and drop outliers, then display the cleaned dataframe.

## Results
- ### KMeans Clustering:
    - Identified 5 clusters with distinct characteristics.
    - Visualized clusters and their centers.
    - Calculated mean values for each cluster.

- ### DBSCAN Clustering:
    - Identified clusters and outliers.
    - Visualized clusters and their centers.
    - Calculated mean values for filtered clusters (excluding outliers).

- ### Cluster Evaluation:
    - Silhouette Score for KMeans: `0.5547`
    - Silhouette Score for DBSCAN (outliers removed): `0.5972`


## Conclusion
Based on the silhouette scores, DBSCAN (with outliers removed) performed slightly better than KMeans for this dataset. The analysis helps to identify different customer segments, enabling businesses to tailor their marketing strategies to target specific groups effectively.
