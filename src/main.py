import argparse
from extract_station_id import extract_station_id
from download_weather_data import download_weather_data
#from merge_data import merge_data



def main(city, year):
    # Step 1: Retrieve the station ID for the input city
    station_id = extract_station_id(city)
    
    # Step 2: Download the weather data for the input year and the previous two years
    download_weather_data(station_id, year)
    #download_weather_data(station_id, year-1)
    #download_weather_data(station_id, year-2)
    
    # Step 3: Merge and clean up the data
    #merged_data = merge_data(city, year)
    
    # ... (subsequent steps will go here)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Weather data ETL process')
    parser.add_argument('--city', type=str, required=True, help='City to retrieve the weather data for')
    parser.add_argument('--year', type=int, required=True, help='Year to retrieve the weather data for')
    
    args = parser.parse_args()
    
    main(args.city, args.year)