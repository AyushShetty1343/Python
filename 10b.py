import json
# Load the JSON data from file
with open("/Users/ayushshetty/Desktop/Python/weather.json") as f:
    data = json.load(f)
 # Extract the required weather data
current_temp = data['main']['temp']
humidity = data['main']['humidity']
weather_desc = data['main']['condition']
# Display the weather data
print(f"Current temperature: {current_temp}°C")
print(f"Humidity: {humidity}%")
print(f"Weather description: {weather_desc}")
