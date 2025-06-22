import pandas as pd

# Load the dataset
df = pd.read_csv("restaurant_data.csv")

# Display the first few rows
print(df.head())


# Count how many times each restaurant name appears
restaurant_counts = df['Restaurant Name'].value_counts()

# Filter restaurants that appear more than once (chains)
chains = restaurant_counts[restaurant_counts > 1]

# Display top 10 restaurant chains
print("\nTop 10 Restaurant Chains (by number of branches):")
print(chains.head(10))


# Filter the original DataFrame to include only restaurant chains
df_chains = df[df['Restaurant Name'].isin(chains.index)]

# Group by restaurant name and calculate average rating and average votes
chain_analysis = df_chains.groupby('Restaurant Name').agg({
    'Aggregate rating': 'mean',
    'Votes': 'mean',
    'Restaurant Name': 'count'  # Optional: number of branches
}).rename(columns={'Restaurant Name': 'Number of Branches'})

# Sort by average rating (highest rated chains first)
chain_analysis_sorted = chain_analysis.sort_values(by='Aggregate rating', ascending=False)

# Display the top 10 highest rated chains
print("\nTop 10 Restaurant Chains by Average Rating:")
print(chain_analysis_sorted.head(10).round(2))
