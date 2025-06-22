import pandas as pd

# Load dataset
df = pd.read_csv("restaurant_data.csv")

# Display first few rows
print(df.head())


# Drop rows with missing values in the 'Cuisines' column
df = df.dropna(subset=['Cuisines'])

# Strip extra spaces and normalize combinations
df['Cuisines'] = df['Cuisines'].apply(lambda x: ', '.join(sorted([c.strip() for c in x.split(',')])))

# Count the most common combinations
common_combinations = df['Cuisines'].value_counts().head(10)

# Display top 10 most common cuisine combinations
print("\nTop 10 Most Common Cuisine Combinations:")
print(common_combinations)


# Group by cuisine combinations and calculate average rating
rating_by_cuisine_combo = df.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending=False)

# Display top 10 combinations with the highest average ratings
print("\nTop 10 Cuisine Combinations with Highest Average Ratings:")
print(rating_by_cuisine_combo.head(10).round(2))

