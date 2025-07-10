import requests

base_url = ""
key = "20001e9c835eedce6a71a11b197ab92b"

def get_weather_info(city_name, key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}"
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        weather_data = response.json()

        for key, value in weather_data.items():
            return weather_data

    else:
        print(f"Not found {response.status_code}")

city = input("Enter a city name: ")
weather_info = get_weather_info(city, key)

print(weather_info["id"])
print(weather_info["name"])
print(weather_info["main"]["temp"])
print(weather_info["main"]["humidity"])
print(f"Wheather: {weather_info["weather"][0]["main"]} \nClouds: {weather_info["weather"][0]["description"]}")