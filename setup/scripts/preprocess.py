
import geopandas as gpd
from shapely.geometry import Point



def preprocess_fire(fire_data):
    """Process fire data (CSV or API response) into a GeoDataFrame."""
    fire_df = gpd.GeoDataFrame(fire_data, geometry=gpd.points_from_xy(fire_data['longitude'], fire_data['latitude']))
    fire_df.set_geometry('geometry', inplace=True)
    fire_df["latitude"] = fire_df.geometry.y
    fire_df["longitude"] = fire_df.geometry.x
    return fire_df


if __name__ == "__main__":
    # Example fire data with 'latitude' and 'longitude' columns
    # fire_sample = {
    #     'latitude': [34.0522, 35.0522, 36.0522],
    #     'longitude': [-118.2437, -119.2437, -120.2437],
    #     'intensity': [5, 3, 8]
    # }
    fire_sample = {
    'latitude': [34.0522, 35.0522, 36.0522, 37.1522, 33.9522, 34.7522],
    'longitude': [-118.2437, -119.2437, -120.2437, -121.3437, -117.8437, -118.5437],
    'intensity': [5, 3, 8, 6, 4, 7]
    }
    
    fire_data = preprocess_fire(fire_sample)
    print(fire_data)
