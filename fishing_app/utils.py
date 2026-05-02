import requests

# Keep weather data ( real-time ) --> send to place_detail func


def get_weather_data(lat, lon):

    api_key = "3e4585b26548cd46e046be97cc79ac48"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather = {
                'temp': round(data['main']['temp']),
                'wind_speed': data['wind']['speed'],
                'pressure': data['main']['pressure'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }
            return weather

    except Exception as e:
        print(f"Timekeeping error: {e}")

    return None
