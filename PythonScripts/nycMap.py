# A44
# NYC Map

import folium

# Create a map centered around the given coordinates with a specific zoom level
mapCUNY = folium.Map(location=[40.75, -74.125], zoom_start=10)

# Add a marker for Hunter College to the map
folium.Marker(location=[40.768731, -73.964915], popup="Hunter College").add_to(mapCUNY)

# Save the map to an HTML file
mapCUNY.save(outfile='nycMap.html')

