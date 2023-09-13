import pandas as pd
from pathlib import Path

def merge_data(city, year):
    # Step 1: Load the Station Inventory Data
    station_inventory_path = Path('/media/tak/DATA/work/wave/data/station_inventory.csv')
    station_inventory_data = pd.read_csv(station_inventory_path)
    
    # Step 2: Load the Weather Data
    weather_data = []
    for y in range(year-2, year+1):
        for month in range(1, 13):
            weather_data_path = Path(f'/media/tak/DATA/work/wave/data/weather_data/{y}/{month}.csv')
            if weather_data_path.exists():
                monthly_data = pd.read_csv(weather_data_path)
                weather_data.append(monthly_data)
    
    weather_data = pd.concat(weather_data, ignore_index=True)
    
    # Step 3: Merge the Data
    # Extract the station ID for the specified city
    station_id = station_inventory_data.loc[station_inventory_data['Name'].str.upper() == city.upper(), 'Station ID'].values[0]
    
    # Merge the station inventory data with the weather data
    merged_data = pd.merge(weather_data, station_inventory_data, how='inner', left_on='Station ID', right_on='Station ID')
    
    return merged_data

# Call the function to test it
merged_data = merge_data('Toronto', 2021)
print(merged_data.head())
