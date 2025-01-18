# import pandas as pd
# import geopandas as gpd

# def preprocess_weather(weather_data):
#     return {
#         "temperature": weather_data["main"]["temp"] - 273.15,  # Convert Kelvin to Celsius
#         "humidity": weather_data["main"]["humidity"],
#         "wind_speed": weather_data["wind"]["speed"],
#         "wind_direction": weather_data["wind"]["deg"]
#     }

# def preprocess_fire(fire_data):
#     fire_df = gpd.GeoDataFrame.from_features(fire_data["features"])
#     return fire_df

# if __name__ == "__main__":
#     # Example testing
#     weather_sample = {"main": {"temp": 300, "humidity": 40}, "wind": {"speed": 5, "deg": 180}}
#     fire_sample = {"features": []}  # Replace with real fire data
#     print(preprocess_weather(weather_sample))

import geopandas as gpd
from shapely.geometry import Point

# def preprocess_fire(fire_data):
#     """Process fire data (CSV or API response) into a GeoDataFrame."""
#     # Example of fire_data to be processed
#     fire_df = gpd.GeoDataFrame(fire_data, geometry=gpd.points_from_xy(fire_data['longitude'], fire_data['latitude']))
    
#     # Ensure the 'geometry' column is set
#     fire_df.set_geometry('geometry', inplace=True)
    
#     # Now, you can access the latitude and longitude via geometry
#     fire_df["latitude"] = fire_df.geometry.y
#     fire_df["longitude"] = fire_df.geometry.x
    
#     return fire_df

def preprocess_fire(fire_data):
    """Process fire data (CSV or API response) into a GeoDataFrame."""
    fire_df = gpd.GeoDataFrame(fire_data, geometry=gpd.points_from_xy(fire_data['longitude'], fire_data['latitude']))
    fire_df.set_geometry('geometry', inplace=True)
    fire_df["latitude"] = fire_df.geometry.y
    fire_df["longitude"] = fire_df.geometry.x
    return fire_df


if __name__ == "__main__":
    # Example fire data with 'latitude' and 'longitude' columns
    fire_sample = {
        'latitude': [34.0522, 35.0522, 36.0522],
        'longitude': [-118.2437, -119.2437, -120.2437],
        'intensity': [5, 3, 8]
    }
    
    fire_data = preprocess_fire(fire_sample)
    print(fire_data)
