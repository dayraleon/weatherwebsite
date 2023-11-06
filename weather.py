import requests

def getweather(api_key, city):
    base_url = "https://api.weatherbit.io/v2.0/current"
    params = {
        "city": city,
        "key": api_key,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather_data = data['data'][0]
        temperature = weather_data['temp']
        description = weather_data['weather']['description']


        tempf = (temperature * 9/5) + 32

        print(f"Weather in {city}:")
        print(f"Temperature: {tempf}F")
        print(f"Description: {description}")
    else:
        print(f"Failed to fetch weather data for {city}")

if __name__ == "__main__":
    api_key = 'd0c85e18d290455ab55b46fa34201f37'  # Replace with your OpenWeatherMap API key
    city = input("Enter the city name: ")
    getweather(api_key,city)
