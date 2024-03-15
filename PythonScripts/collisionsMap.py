import folium
import pandas as pd

# Ask user for input file and output file names
file = input("Enter CSV file name: ")       # collisionsMap.csv
output = input("Enter output file: ")       # collisionsMap.html

# Read the CSV file into a DataFrame
collisions_data = pd.read_csv(file)

# Filter out rows where longitude is not blank
collisions_data = collisions_data.dropna(subset=['LONGITUDE'])

# Create a Folium map centered at a specific location
map_collisions = folium.Map(location=[40.768731, -73.964915], tiles="Cartodb Positron", zoom_start=12)

# Iterate over each row in the DataFrame
for index, row in collisions_data.iterrows():
    # Extract latitude and longitude from the DataFrame
    lat = float(row["LATITUDE"])
    lon = float(row["LONGITUDE"])

    # Create a new marker for each location with a popup message
    popup_msg = f"Collision occurred at {row['TIME']}"
    new_marker = folium.Marker([lat, lon], popup=popup_msg)

    # Add the marker to the map
    new_marker.add_to(map_collisions)

# Save the map to the specified output file
map_collisions.save(output)
