
# from scripts.fetch_fire import fetch_fire_data



# def main():
#     # Fetch fire data as CSV
#     fire_api_key = "bb9be6f693d302f51c29fdf7667724b4"  # Replace with your actual API key
#     date_of_interest = "2025-01-18"

#     try:
#         fire_csv_data = fetch_fire_data(fire_api_key, date=date_of_interest)

#         # Save to a CSV file
#         with open("fire_data.csv", "w") as file:
#             file.write(fire_csv_data)
#             print("Fire data CSV saved successfully as 'fire_data.csv'.")
    
#     except Exception as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     main()





# from scripts.fetch_fire import fetch_fire_data
# from scripts.preprocess import preprocess_fire

# # from scripts.preprocess import preprocess_fire, preprocess_weather
# from models.spread_model.spread_simulation import spread_fire
# from visualizations.map_visualizer import visualize_fire

# def main():
#     # Fetch fire data and weather parameters
#     fire_api_key = "bb9be6f693d302f51c29fdf7667724b4"  # Replace with your actual API key
#     date_of_interest = "2025-01-18"

#     try:
#         # Fetch the fire data (CSV format)
#         fire_csv_data = fetch_fire_data(fire_api_key, date=date_of_interest)
        
#         # Process the fire data into GeoDataFrame
#         fire_data = preprocess_fire(fire_csv_data)
        
#         # Extract environmental parameters (e.g., wind speed, temperature) for simulation
#         weather_data = {"main": {"temp": 300, "humidity": 40}, "wind": {"speed": 5, "deg": 180}}  # Replace with actual weather data
#         weather_params = preprocess_weather(weather_data)
        
#         # Set up a grid representing fire areas (this would depend on the fire data)
#         grid = np.zeros((10, 10))  # Example grid, replace with real data
#         grid[5, 5] = 1  # Initial fire point
        
#         # Simulate the fire spread based on weather parameters (e.g., wind speed)
#         fire_spread = spread_fire(grid, wind_speed=weather_params['wind_speed'], wind_direction=weather_params['wind_direction'], iterations=10)
        
#         # Visualize the fire spread on a map
#         for lat, lon in zip(fire_data['latitude'], fire_data['longitude']):  # Assume fire_data has latitude/longitude columns
#             visualize_fire(lat, lon, radius=10)
        
#         # Optionally, save the fire spread data for later use
#         print(f"Fire spread simulation complete. Data visualized on map.")
        
#     except Exception as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     main()


import pandas as pd
from scripts.fetch_fire import fetch_fire_data
from scripts.preprocess import preprocess_fire

def main():
    # Fetch fire data as CSV
    fire_api_key = "bb9be6f693d302f51c29fdf7667724b4"  # Replace with your actual API key
    date_of_interest = "2025-01-18"

    try:
        fire_csv_data = fetch_fire_data(fire_api_key, date=date_of_interest)

        # Parse the CSV string into a DataFrame
        from io import StringIO
        fire_data_df = pd.read_csv(StringIO(fire_csv_data))

        # Preprocess the fire data
        fire_df = preprocess_fire(fire_data_df)

        # Save to a CSV file
        fire_df.to_csv("fire_data.csv", index=False)
        print("Fire data CSV saved successfully as 'fire_data.csv'.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
