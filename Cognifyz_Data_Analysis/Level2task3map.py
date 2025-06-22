import pandas as pd
import folium
from folium.plugins import HeatMap

# Load dataset
df = pd.read_csv("restaurant_data.csv")

# Display the first few rows
print(df.head())


# Drop rows with missing latitude or longitude
df = df.dropna(subset=['Latitude', 'Longitude'])

# Create a base map centered on the average location
map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
restaurant_map = folium.Map(location=map_center, zoom_start=11)


# Add restaurant markers to the map
for index, row in df.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=2,
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.6
    ).add_to(restaurant_map)


# Save the map to an HTML file
restaurant_map.save("restaurant_map.html")
print("Map saved as restaurant_map.html")


# Create a new map for the heatmap
heatmap_map = folium.Map(location=map_center, zoom_start=11)

# Prepare data: list of [lat, lon] points
heat_data = df[['Latitude', 'Longitude']].values.tolist()

# Add the heatmap layer
HeatMap(heat_data, radius=10).add_to(heatmap_map)

# Save heatmap to HTML
heatmap_map.save("restaurant_heatmap.html")
print("Heatmap saved as restaurant_heatmap.html")
