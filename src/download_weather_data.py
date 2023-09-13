import os

def download_weather_data(station_id):
    # Base URL for downloading the data
    base_url = "https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv"
    
    # Directory to save the downloaded data
    data_dir = "data/weather_data"
    os.makedirs(data_dir, exist_ok=True)
    
    # Loop through the years and months and download the data
    for year in range(2018, 2022):
        for month in range(1, 13):
            # Construct the URL to download the data
            url = f"{base_url}&stationID={station_id}&Year={year}&Month={month}&Day=14&timeframe=2&submit=Download+Data"
            
            # Construct the command to download the data
            command = f'wget --content-disposition -P {data_dir} "{url}"'
            
            # Execute the command
            os.system(command)

# Uncomment the following line to run the function with the station ID as the argument
download_weather_data(5651)