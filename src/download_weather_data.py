import os

def download_weather_data(station_id, year):
    # Base URL for downloading the data
    base_url = "https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv"
    
    # Directory to save the downloaded data
    data_dir = f"/media/tak/DATA/work/wave/data/weather_data/"
    os.makedirs(data_dir, exist_ok=True)
    month = 1
    # Loop through the months and download the data
    #for month in range(1, 13):
        # Construct the URL to download the data
    url = f"{base_url}&stationID={station_id}&Year={year}&Month={month}&Day=14&timeframe=3&submit=Download+Data"
    filename = f"{year}_{month}_weather_data.csv"
        # Construct the command to download the data
    command = f'wget --content-disposition -P {data_dir}/{filename} "{url}"'
        
        # Execute the command
    os.system(command)