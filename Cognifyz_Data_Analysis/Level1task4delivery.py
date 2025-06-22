import pandas as pd

# Load dataset
df = pd.read_csv("restaurant_data.csv")

# Display first 5 rows to check the dataset
print(df.head())


# Count the number of restaurants offering and not offering online delivery
delivery_counts = df['Has Online delivery'].value_counts()

# Calculate the percentage
total_restaurants = len(df)
delivery_percentage = (delivery_counts / total_restaurants) * 100

# Display the results
print("\nPercentage of Restaurants Offering Online Delivery:")
print(delivery_percentage.round(2))  # Round to 2 decimal places


# Calculate average rating for restaurants WITH online delivery
avg_rating_with_delivery = df[df['Has Online delivery'] == 'Yes']['Aggregate rating'].mean()

# Calculate average rating for restaurants WITHOUT online delivery
avg_rating_without_delivery = df[df['Has Online delivery'] == 'No']['Aggregate rating'].mean()

# Display the results
print(f"\nAverage Rating of Restaurants Offering Online Delivery: {avg_rating_with_delivery:.2f}")
print(f"Average Rating of Restaurants NOT Offering Online Delivery: {avg_rating_without_delivery:.2f}")

