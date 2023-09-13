import pandas as pd

def extract_station_id():
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv('data/station_inventory_en.csv')

    
    # Filter the DataFrame to get a record for a weather station in Toronto, Ontario
    # (You might need to adjust the filtering conditions based on the structure of the CSV file)
    toronto_station = df[(df['Name'] == 'TORONTO')]
    
    # Extract the station ID
    if not toronto_station.empty:
        station_id = toronto_station['Station ID'].values[0]
        print(f"The station ID for Toronto, Ontario is: {station_id}")
        return station_id
    else:
        print("No station found with the exact name 'TORONTO'")
        return None

# Uncomment the following line to run the function
extract_station_id()