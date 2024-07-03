import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
players_data = pd.read_csv('data/Players.csv')

# Display the first few rows of the dataset
print("\nFirst few rows of the dataset:")
print(players_data.head())

# Summary statistics for numerical columns
print("\nSummary Statistics for Numerical Columns:")
print(players_data.describe())

# Distribution of players by height
plt.figure(figsize=(12, 6))
sns.histplot(players_data['height'], bins=20, kde=True)
plt.title('Distribution of Players by Height')
plt.xlabel('Height')
plt.ylabel('Count')
plt.show()

# Distribution of players by weight
plt.figure(figsize=(12, 6))
sns.histplot(players_data['weight'], bins=20, kde=True)
plt.title('Distribution of Players by Weight')
plt.xlabel('Weight')
plt.ylabel('Count')
plt.show()

# Universities that produced the most NBA players
plt.figure(figsize=(12, 10))
top_colleges = players_data['collage'].value_counts().head(20)
sns.barplot(y=top_colleges.index, x=top_colleges.values, palette='viridis')
plt.title('Top 20 Universities by Number of NBA Players Produced')
plt.xlabel('Number of Players')
plt.ylabel('University')
plt.xticks(fontsize=10)
plt.yticks(fontsize=8)
plt.show()
