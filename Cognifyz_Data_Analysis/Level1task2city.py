import pandas as pd

# Load dataset
df = pd.read_csv("restaurant_data.csv")

# Display first 5 rows to check the dataset
print(df.head())


# Count the number of restaurants in each city
city_counts = df['City'].value_counts()

# Get the city with the highest number of restaurants
top_city = city_counts.idxmax()
top_city_count = city_counts.max()

# Display the results
print(f"\nCity with the Highest Number of Restaurants: {top_city} ({top_city_count} restaurants)")


# Calculate the average rating for restaurants in each city
city_avg_rating = df.groupby('City')['Aggregate rating'].mean()

# Display the first 10 cities and their average ratings
print("\nAverage Rating for Each City:")
print(city_avg_rating.head(10))  # Display first 10 cities


# Find the city with the highest average rating
top_rated_city = city_avg_rating.idxmax()
top_rated_value = city_avg_rating.max()

# Display the result
print(f"\nCity with the Highest Average Rating: {top_rated_city} ({top_rated_value:.2f} rating)")

