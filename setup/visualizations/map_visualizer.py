
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
