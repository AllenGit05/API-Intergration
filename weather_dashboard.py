import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

API_KEY = '05f18e650b9f73117e5aed357fc59ec2'  # Your API key
CITY = 'London'                               # You can change this to any city you like
UNITS = 'metric'                              # 'metric' = Celsius, 'imperial' = Fahrenheit

URL = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units={UNITS}'

def fetch_weather_data():
    try:
        response = requests.get(URL)
        data = response.json()

        if response.status_code != 200 or 'list' not in data:
            print("❌ Error fetching data from API:")
            print(data.get('message', 'Unknown error'))
            exit(1)
        return data['list']
    
    except requests.exceptions.RequestException as e:
        print("❌ Network error:", e)
        exit(1)

def parse_weather_data(data):
    dates = []
    temps = []
    humidity = []
    
    for entry in data:
        dt = datetime.fromtimestamp(entry['dt'])
        temp = entry['main']['temp']
        hum = entry['main']['humidity']
        
        dates.append(dt)
        temps.append(temp)
        humidity.append(hum)
    return dates, temps, humidity

def create_visualizations(dates, temps, humidity):
    sns.set(style="whitegrid")
    plt.figure(figsize=(14, 6))

    # Temperature Plot
    plt.subplot(1, 2, 1)
    sns.lineplot(x=dates, y=temps, color='blue', marker='o')
    plt.title(f'Temperature Over Time in {CITY}')
    plt.xlabel('Date and Time')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)

    # Humidity Plot
    plt.subplot(1, 2, 2)
    sns.lineplot(x=dates, y=humidity, color='green', marker='o')
    plt.title(f'Humidity Over Time in {CITY}')
    plt.xlabel('Date and Time')
    plt.ylabel('Humidity (%)')
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()

def main():
    print(f"Fetching weather data for {CITY}...")
    data = fetch_weather_data()
    dates, temps, humidity = parse_weather_data(data)
    print("Creating visualizations...")
    create_visualizations(dates, temps, humidity)

if __name__ == '__main__':
    main()
