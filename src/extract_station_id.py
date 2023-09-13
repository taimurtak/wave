import pandas as pd

def extract_station_id(city):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv('/media/tak/DATA/work/wave/data/station_inventory.csv')
    
    
    # Filter the DataFrame to get a record for the input city in Ontario
    city_station = df[df['Name'].str.upper() == city.upper()]
    
    # Extract and return the station ID
    if not city_station.empty:
        #print(city_station['Station ID'].values[0])
        return city_station['Station ID'].values[0]

    else:
        print(f"No station found for the city: {city}")
        return None
    
#extract_station_id("Toronto")
