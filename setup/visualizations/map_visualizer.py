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


import folium

def visualize_fire(lat, lon, radius=10):
    """
    Visualizes the fire on a map using Folium.
    
    :param lat: Latitude of the fire location.
    :param lon: Longitude of the fire location.
    :param radius: Radius of the fire spread (in km).
    """
    m = folium.Map(location=[lat, lon], zoom_start=10)
    
    # Create a red circle to represent fire spread
    folium.Circle([lat, lon], radius=radius * 1000, color="red", fill=True).add_to(m)
    
    # Save the map to an HTML file
    m.save("visualizations/fire_map.html")

if __name__ == "__main__":
    # Example: You can update the radius based on the simulation's results
    visualize_fire(34.0522, -118.2437, radius=10)  # Fire at Los Angeles with a 10 km radius
