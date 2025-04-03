import requests
import pandas as pd
from apscheduler.schedulers.background import BackgroundScheduler
import time
import os

# Configuration
API_KEY = '45bea71c90644b23902102541250204'  # Replace with your WeatherAPI key
CITY = 'London'
CSV_FILE = 'weather_data.csv'

def create_csv_if_not_exists():
    # Check if the CSV file exists
    if not os.path.exists(CSV_FILE):
        # Create the CSV file with the header if it doesn't exist
        df = pd.DataFrame(columns=['timestamp', 'city', 'temperature', 'weather', 'humidity', 'wind_speed'])
        df.to_csv(CSV_FILE, index=False)
        print("CSV file created.")

def fetch_weather_data():
    url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}'
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        print(f"Error fetching data: {data.get('error', {}).get('message', 'Unknown error')}")
        return

    weather_info = {
        'timestamp': pd.Timestamp.now(),
        'city': data['location']['name'],
        'temperature': data['current']['temp_c'],  # temperature in Celsius
        'weather': data['current']['condition']['text'],
        'humidity': data['current']['humidity'],
        'wind_speed': data['current']['wind_kph']  # wind speed in km/h
    }

    df = pd.DataFrame([weather_info])
    df.to_csv(CSV_FILE, mode='a', header=not pd.read_csv(CSV_FILE).empty, index=False)
    print("Weather data saved to CSV.")

# Create CSV file if it doesn't exist
create_csv_if_not_exists()

scheduler = BackgroundScheduler()
scheduler.add_job(fetch_weather_data, 'interval', seconds=10)
scheduler.start()

# Keep the script running to allow the scheduled task to execute
try:
    while True:
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
