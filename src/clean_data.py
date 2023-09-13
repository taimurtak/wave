import pandas as pd
from pathlib import Path
from datetime import datetime

def clean_data(year):
    # Load the data
    data_dir = Path(f'/media/tak/DATA/work/wave/data/weather_data/2021_1_weather_data.csv/en_climate_monthly_ON_6158350_1840-2006_P1M.csv')
    data_files = data_dir.glob('*.csv')
    data_frames = [pd.read_csv(file) for file in data_files]
    data = pd.concat(data_frames, ignore_index=True)
    
    # Convert date column to datetime
    data['Date/Time'] = pd.to_datetime(data['Date/Time'])
    
    # 1. Remove Future Dates
    today = datetime.today()
    data = data[data['Date/Time'] <= today]
    
    # 2. Handle Missing Data
    data = data[data['Mean Temp (°C)'].notna()]
    
    # 3. Drop Unnecessary Columns
    # List the columns to be dropped here (this is just an example, update based on your data)
    columns_to_drop = ['Column1', 'Column2']
    data = data.drop(columns=columns_to_drop, errors='ignore')
    
    return data


cleaned_data = clean_data(2021)
print(cleaned_data.head())
