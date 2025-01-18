# import numpy as np

# def spread_fire(grid, wind_speed, wind_direction, iterations=10):
#     for _ in range(iterations):
#         # Simulate fire spread (placeholder logic)
#         grid = np.pad(grid, pad_width=1, mode='constant')
#         grid = np.roll(grid, shift=int(wind_speed), axis=1)  # Simulate wind spread
#     return grid

# if __name__ == "__main__":
#     grid = np.zeros((10, 10))
#     grid[5, 5] = 1  # Initial fire
#     spread = spread_fire(grid, wind_speed=2, wind_direction=90, iterations=5)
#     print(spread)




# import numpy as np




# def spread_fire(grid, wind_speed, wind_direction, iterations=10):
#     for _ in range(iterations):
#         # Simulate fire spread based on wind speed and direction (simplified)
#         grid = np.pad(grid, pad_width=1, mode='constant')  # Expand grid
#         grid = np.roll(grid, shift=int(wind_speed), axis=1)  # Simple wind simulation by shifting columns
#     return grid

# if __name__ == "__main__":
#     grid = np.zeros((10, 10))
#     grid[5, 5] = 1  # Initial fire at the center
#     spread = spread_fire(grid, wind_speed=2, wind_direction=90, iterations=5)
#     print(spread)



import numpy as np
from visualizations.map_visualizer import visualize_fire  # Absolute import

def spread_fire(grid, wind_speed, wind_direction, iterations=10):
    """
    Simulates fire spread across a grid based on wind speed and direction.
    
    :param grid: A 2D grid representing the area, where 1 indicates fire, 0 indicates no fire.
    :param wind_speed: The speed of the wind affecting fire spread.
    :param wind_direction: The direction of the wind (degrees).
    :param iterations: The number of simulation steps (time iterations) to run.
    :return: A grid with the fire spread and the radius of the fire's spread.
    """
    for _ in range(iterations):
        # Simulate fire spread with simple logic (expand fire in the direction of the wind)
        grid = np.pad(grid, pad_width=1, mode='constant')
        grid = np.roll(grid, shift=int(wind_speed), axis=1)  # Simple wind spread simulation
        
    # Calculate the radius of the fire based on the grid
    fire_radius = np.sum(grid) ** 0.5  # Placeholder for radius calculation (rough estimate)
    return grid, fire_radius

if __name__ == "__main__":
    # Example simulation: 10x10 grid, initial fire at the center, wind from the east (90 degrees)
    grid = np.zeros((10, 10))
    grid[5, 5] = 1  # Initial fire in the center
    
    # Simulate fire spread with wind speed 2, and direction 90 degrees
    spread, radius = spread_fire(grid, wind_speed=2, wind_direction=90, iterations=5)
    
    # Visualize the fire's spread using the calculated radius
    print(f"Fire radius: {radius} km")
    visualize_fire(34.0522, -118.2437, radius=radius)  # Update with actual location and spread
