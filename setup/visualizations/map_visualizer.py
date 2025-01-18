# import folium

# def visualize_fire(lat, lon, radius=10):
#     m = folium.Map(location=[lat, lon], zoom_start=10)
#     folium.Circle([lat, lon], radius=radius * 100, color="red", fill=True).add_to(m)
#     m.save("visualizations/fire_map.html")

# if __name__ == "__main__":
#     visualize_fire(34.0522, -118.2437)


# import folium

# def visualize_fire(lat, lon, radius=10):
#     """Visualize the fire on a map using folium."""
#     m = folium.Map(location=[lat, lon], zoom_start=10)
#     folium.Circle([lat, lon], radius=radius * 100, color="red", fill=True).add_to(m)
#     m.save(f"visualizations/fire_map_{lat}_{lon}.html")  # Save with unique name for each fire location

# if __name__ == "__main__":
#     visualize_fire(34.0522, -118.2437)


# import folium

# def visualize_fire(lat, lon, radius=10):
#     """
#     Visualizes the fire on a map using Folium.
    
#     :param lat: Latitude of the fire location.
#     :param lon: Longitude of the fire location.
#     :param radius: Radius of the fire spread (in km).
#     """
#     m = folium.Map(location=[lat, lon], zoom_start=10)
    
#     # Create a red circle to represent fire spread
#     folium.Circle([lat, lon], radius=radius * 1000, color="red", fill=True).add_to(m)
    
#     # Save the map to an HTML file
#     m.save("visualizations/fire_map.html")

# if __name__ == "__main__":
#     # Example: You can update the radius based on the simulation's results
#     visualize_fire(34.0522, -118.2437, radius=10)  # Fire at Los Angeles with a 10 km radius


import os
import folium

def visualize_fire(latitude, longitude, radius=10):
    # Create a map centered around the fire location
    m = folium.Map(location=[latitude, longitude], zoom_start=12)

    # Add a circle to represent the fire spread
    folium.Circle(
        location=[latitude, longitude],
        radius=radius * 1000,  # Convert to meters
        color='red',
        fill=True,
        fill_opacity=0.5
    ).add_to(m)

    # Get the current directory of this script
    current_dir = os.path.dirname(os.path.realpath(__file__))

    # Save the map to an HTML file in the same folder
    m.save(os.path.join(current_dir, "fire_map.html"))

if __name__ == "__main__":
    visualize_fire(34.0522, -118.2437, radius=10)  # Fire at Los Angeles with a 10 km radius
