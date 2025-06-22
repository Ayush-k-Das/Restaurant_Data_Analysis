import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("restaurant_data.csv")

# Display first few rows
print(df.head())


# Plot the distribution of aggregate ratings
plt.figure(figsize=(8, 5))
plt.hist(df['Aggregate rating'], bins=10, color='skyblue', edgecolor='black')

# Add labels and title
plt.xlabel("Aggregate Rating")
plt.ylabel("Number of Restaurants")
plt.title("Distribution of Restaurant Ratings")

# Show the plot

# Find the most common aggregate rating
most_common_rating = df['Aggregate rating'].mode()[0]
print(f"\nMost Common Aggregate Rating: {most_common_rating}")


# Calculate the average number of votes
average_votes = df['Votes'].mean()

# Display the result
print(f"\nAverage Number of Votes Received by Restaurants: {average_votes:.2f}")


plt.show()
