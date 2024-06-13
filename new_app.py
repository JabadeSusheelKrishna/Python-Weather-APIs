"""
Below code fetches data from weather and Geolocation
APIs using the location by handling errors
"""

import requests
from colorama import Fore, init

init(autoreset=True)
APIKEY = "07e213c2132eda0e9013476bed601071"

def print_weather_data(data):
    """
    This Function prints the Data returned by weather API
    in colourful format by handling the Data NULL errors.

    input : Dictionary (weather API response)

    output : Colourful Data on screen.
    """
    city = data['city']
    weather_list = data['list']

    # Print city information
    print(f"{Fore.CYAN}City: {city['name']}, {city['country']}")
    print(f"Coordinates: {city['coord']['lat']}, {city['coord']['lon']}")
    print(f"Population: {city['population']}")
    print(f"Timezone: {city['timezone']}")
    print(f"Sunrise: {city['sunrise']}")
    print(f"Sunset: {city['sunset']}")
    print("\n" + "="*40 + "\n")

    # Print weather data
    for weather in weather_list:
        dt_txt = weather['dt_txt']
        main = weather['main']
        weather_desc = weather['weather'][0]
        clouds = weather['clouds']
        wind = weather['wind']
        visibility = weather['visibility']
        pop = weather['pop']
        sys = weather['sys']

        print(f"{Fore.YELLOW}Date and Time: {dt_txt}")
        print(f"{Fore.GREEN}Temperature: {main['temp']}K (Feels like: {main['feels_like']}K)")
        print(f"Min Temperature: {main['temp_min']}K, Max Temperature: {main['temp_max']}K")
        print(f"Pressure: {main['pressure']} hPa, Sea Level: {main['sea_level']} hPa, Ground Level: {main['grnd_level']} hPa")
        print(f"Humidity: {main['humidity']}%")
        print(f"Temperature Adjustment: {main['temp_kf']}K")

        print(f"{Fore.BLUE}Weather: {weather_desc['main']} - {weather_desc['description']}")
        print(f"Cloudiness: {clouds['all']}%")
        print(f"{Fore.CYAN}Wind Speed: {wind['speed']} m/s, Direction: {wind['deg']}°, Gust: {wind['gust']} m/s")
        print(f"Visibility: {visibility} meters")
        print(f"Probability of Precipitation: {pop}")
        
        if 'rain' in weather:
            print(f"{Fore.MAGENTA}Rain Volume (last 3 hours): {weather['rain']['3h']} mm")
        
        print(f"Part of Day: {sys['pod']}")
        print("\n" + "="*40 + "\n")

def fetch_coordinates(place):
    """
    This Function fetches the coordinates of a place
    using geolocation API provided by openweather.com

    input : city name as string with state and country code
    output : location list
            => 0 : Latitude
            => 1 : Longitude
    """
    url = "http://api.openweathermap.org/geo/1.0/direct?q="+place+"&limit=1&appid=" + APIKEY
    response = requests.request("GET", url)
    answer = []
    if(response.status_code in [201, 200]):
        answer.append(response.json()[0]["lat"])
        answer.append(response.json()[0]["lon"])
    return answer

def fetch_climate(city_name):
    """
    This function fetches the data from weather API
    with the help of City name and API Key

    input : City Name as String

    output : if Data exists : Prints data and returns true
           : else : returns false
    """
    location = fetch_coordinates(city_name)
    if(not location):
        print("Sorry Wrong location")
        return False

    url = "https://api.openweathermap.org/data/2.5/forecast?lat="+str(location[0])+"&lon="+str(location[1])+"&appid="+APIKEY+"&cnt=5"
    response = requests.request("GET", url)
    if(response.status_code in [200, 201]):
        print_weather_data(response.json())
        return True
    print("The City Name : ", city_name, " Incorrect. Please Retry")
    return False

place = input("Enter Your location : ") + ","
place += input("Enter State Code in two letters : ") + ","
place += input("Enter Country Code in two letters : ")
fetch_climate(place)