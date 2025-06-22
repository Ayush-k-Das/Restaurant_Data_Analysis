import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("restaurant_data.csv")

# Display first 5 rows to check the dataset
print(df.head())


# Count the number of restaurants in each price range
price_range_counts = df['Price range'].value_counts().sort_index()

# Plot the bar chart
plt.figure(figsize=(8, 5))
price_range_counts.plot(kind='bar', color=['blue', 'green', 'red', 'purple'])

# Add labels and title
plt.xlabel("Price Range (1 = Cheapest, 4 = Most Expensive)")
plt.ylabel("Number of Restaurants")
plt.title("Price Range Distribution of Restaurants")


# Calculate total number of restaurants
total_restaurants = len(df)

# Calculate the percentage of restaurants in each price range
price_range_percentage = (price_range_counts / total_restaurants) * 100

# Display the percentage values
print("\nPercentage of Restaurants in Each Price Range:")
print(price_range_percentage.round(2))  # Round to 2 decimal places


# show the chart
plt.show()