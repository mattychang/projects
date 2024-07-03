# NBA Player Performance Analysis
## Author: Matthew Chang

This project aims to analyze the performance of NBA players using historical season statistics. The analysis includes data preprocessing, exploratory data analysis, feature engineering, and predictive modeling using machine learning techniques.

## Files Description

- **data/**: Directory containing CSV files with historical NBA player statistics.
  - `player_data.csv`: Player data file.
  - `Players.csv`: Additional player information.
  - `Seasons_Stats.csv`: Season statistics for NBA players.
- **nba_player_analysis.py**: Python script that performs the analysis and modeling of NBA player performance.
- **nba_player_statistics.py**: Python script that performs basic statistics and data analysis on player information.

## Installation

1. Ensure you have Python 3.x installed.
2. Download the project files to your local machine.
3. Install the required Python packages using the following command:
   ```bash
   pip install pandas seaborn matplotlib scikit-learn

## Datasets

The datasets used in this project were taken from Kaggle:
- [NBA Players Stats](https://www.kaggle.com/datasets/drgilermo/nba-players-stats)

## Usage
To run the analysis script, navigate to the project directory and execute the following command:
```bash
python nba_player_analysis.py
```
The script will do the following steps:

1. Load the dataset.
2. Handle missing values using imputation.
3. Perform exploratory data analysis (EDA) including distribution plots and correlation heatmaps.
4. Feature engineering to create new relevant features.
5. Fit and evaluate machine learning models (Linear Regression and Random Forest Regressor).
6. Perform clustering analysis using KMeans.

To run the statistics script, navigate to the project directory and execute the following command:

```bash
python nba_player_statistics.py
```

The script will perform the following steps:

1. Load the dataset.
2. Display summary statistics about the dataset.
3. Visualize the distribution of players by height, weight, and where they went to university.

### Output
The `nba_player_analysis.py` script will display:

1. Initial and processed data samples.
2. Distribution plot of Points Per Game (PPG).
3. Correlation heatmap of numeric features.
4. Mean Squared Error and R^2 Score for Linear Regression and Random Forest models.
5. Scatter plot of Actual vs Predicted Efficiency.
6. Scatter plot of player clusters based on PPG and Efficiency.

The `nba_player_statistics.py` script will display:

1. Summary statistics about the dataset.
2. Distribution of players by height.
3. Distribution of players by weight.
4. The top 20 universities producing NBA players.

### Notes

1. The script handles missing values by imputing the mean for numeric columns.
2. Clustering is performed using KMeans with 3 clusters as default.
3. Model evaluation metrics (MSE and R^2 Score) help in assessing the performance of the regression models.
