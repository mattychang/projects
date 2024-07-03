import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.cluster import KMeans
from sklearn.impute import SimpleImputer

# Load the dataset
file_name = '/data/Seasons_Stats.csv'
data = pd.read_csv(file_name)

# Display the first few rows of the dataset
print(data.head())

# Separate numeric and non-numeric columns
numeric_cols = data.select_dtypes(include=['number']).columns
non_numeric_cols = data.select_dtypes(exclude=['number']).columns

# Drop columns that are entirely NaN or non-numeric
valid_numeric_cols = data[numeric_cols].dropna(axis=1, how='all').columns

# Handle missing values for valid numeric columns
imputer = SimpleImputer(strategy='mean')
imputed_data = pd.DataFrame(imputer.fit_transform(data[valid_numeric_cols]), columns=valid_numeric_cols)

# Ensure non-numeric columns are kept intact
data[non_numeric_cols] = data[non_numeric_cols].fillna('Unknown')

# Reassign the imputed numeric data back to the original DataFrame
data[valid_numeric_cols] = imputed_data

# Display the first few rows of the dataset after imputation
print(data.head())

# Feature engineering (e.g., Points Per Game, Efficiency Rating)
data['PPG'] = data['PTS'] / data['G']
data['Efficiency'] = (data['PTS'] + data['TRB'] + data['AST'] + data['STL'] + data['BLK']) - \
                     ((data['FGA'] - data['FG']) + (data['FTA'] - data['FT']) + data['TOV'])

# Exploratory Data Analysis (EDA)

# Distribution of Points Per Game
sns.histplot(data['PPG'], bins=20)
plt.title('Distribution of Points Per Game')
plt.xlabel('Points Per Game')
plt.ylabel('Frequency')
plt.show()

# Correlation heatmap without annotations
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(numeric_only=True), annot=False, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Feature Selection
features = ['PPG', 'TRB', 'AST', 'STL', 'BLK', 'TOV']
X = data[features]
y = data['Efficiency']

# Modeling with Linear Regression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f'Mean Squared Error: {mean_squared_error(y_test, y_pred)}')
print(f'R^2 Score: {r2_score(y_test, y_pred)}')

# Plot predicted vs actual efficiency
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Efficiency')
plt.ylabel('Predicted Efficiency')
plt.title('Actual vs Predicted Efficiency')
plt.show()

# Advanced Analysis - Random Forest Regressor
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

rf_y_pred = rf_model.predict(X_test)
print(f'Random Forest Mean Squared Error: {mean_squared_error(y_test, rf_y_pred)}')
print(f'Random Forest R^2 Score: {r2_score(y_test, rf_y_pred)}')

# Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
data['Cluster'] = kmeans.fit_predict(X)

# Visualize the clusters
sns.scatterplot(data=data, x='PPG', y='Efficiency', hue='Cluster', palette='viridis')
plt.title('Player Clusters')
plt.show()
