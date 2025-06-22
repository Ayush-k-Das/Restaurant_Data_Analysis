import pandas as pd

# Load the dataset
df = pd.read_csv("restaurant_data.csv")

# Display first 5 rows
print(df.head())


# Ensure column names are clean (strip spaces)
df.columns = df.columns.str.strip()

# Split multiple cuisines into separate rows
df['Cuisines'] = df['Cuisines'].str.split(',')

# Convert list entries into separate rows
df_exploded = df.explode('Cuisines')

# Remove extra spaces from cuisine names
df_exploded['Cuisines'] = df_exploded['Cuisines'].str.strip()

# Display the updated data
print(df_exploded[['Restaurant Name', 'Cuisines']].head(10))


# Count occurrences of each cuisine
cuisine_counts = df_exploded['Cuisines'].value_counts()

# Get the top 3 most common cuisines
top_3_cuisines = cuisine_counts.head(3)

# Display the top 3 cuisines
print("\nTop 3 Most Common Cuisines:")
print(top_3_cuisines)


# Count total unique restaurants
total_restaurants = df['Restaurant Name'].nunique()

# Calculate the percentage of restaurants serving each top cuisine
top_cuisines_percentage = (top_3_cuisines / total_restaurants) * 100

# Display the percentages
print("\nPercentage of Restaurants Serving Top Cuisines:")
print(top_cuisines_percentage.round(2))  # Round to 2 decimal places


import matplotlib.pyplot as plt

# Plot the bar chart
plt.figure(figsize=(8, 5))
top_cuisines_percentage.plot(kind='bar', color=['blue', 'green', 'red'])

# Add labels and title
plt.xlabel("Cuisine Type")
plt.ylabel("Percentage of Restaurants (%)")
plt.title("Top 3 Cuisines by Restaurant Percentage")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the chart
plt.show()
