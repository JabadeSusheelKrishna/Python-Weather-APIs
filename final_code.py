"""
Below code fetches data from weather API
using the Location by handling errors
"""

import requests

APIKEY = "07e213c2132eda0e9013476bed601071"     # Get it from open weather webiste

def print_weather_data(dict_data):
    """
    This Function prints the Data returned by weather API
    in colourful format by handling the Data NULL errors.

    input : Dictionary (weather API response)

    output : Colourful Data on screen.
    """
    try:
        if "name" in dict_data:
            print("\033[92mLocation:\033[0m", dict_data["name"])
        else:
            print("\033[91mLocation: Not available\033[0m")

        if "coord" in dict_data:
            print("\033[92mCoordinates:\033[0m")
            if "lat" in dict_data["coord"]:
                print("\033[94m\tLatitude:\033[0m", dict_data["coord"]["lat"])
            else:
                print("\033[91m\tLatitude: Not available\033[0m")
            if "lon" in dict_data["coord"]:
                print("\033[94m\tLongitude:\033[0m", dict_data["coord"]["lon"])
            else:
                print("\033[91m\tLongitude: Not available\033[0m")
        else:
            print("\033[91mCoordinates: Not available\033[0m")

        if "weather" in dict_data and len(dict_data["weather"]) > 0:
            print("\033[92mWeather Conditions:\033[0m")
            weather = dict_data["weather"][0]
            if "main" in weather:
                print("\033[94m\tNature:\033[0m", weather["main"], "(", weather.get("description", "\033[91mDescription not available\033[0m"), ")")
            else:
                print("\033[91m\tNature: Not available\033[0m")
        else:
            print("\033[91mWeather Conditions: Not available\033[0m")

        if "main" in dict_data:
            print("\033[92mTemperature Information:\033[0m")
            main = dict_data["main"]
            print("\033[94m\tTemperature:\033[0m", main.get("temp", "\033[91mNot available\033[0m"))
            print("\033[94m\tFeels Like:\033[0m", main.get("feels_like", "\033[91mNot available\033[0m"))
            print("\033[94m\tMinimum Temperature:\033[0m", main.get("temp_min", "\033[91mNot available\033[0m"))
            print("\033[94m\tMaximum Temperature:\033[0m", main.get("temp_max", "\033[91mNot available\033[0m"))
            print("\033[94m\tPressure:\033[0m", main.get("pressure", "\033[91mNot available\033[0m"))
            print("\033[94m\tHumidity:\033[0m", main.get("humidity", "\033[91mNot available\033[0m"))
        else:
            print("\033[91mTemperature Information: Not available\033[0m")

        if "wind" in dict_data:
            print("\033[92mWind Information:\033[0m")
            wind = dict_data["wind"]
            print("\033[94m\tSpeed:\033[0m", wind.get("speed", "\033[91mNot available\033[0m"))
            print("\033[94m\tDirection:\033[0m", wind.get("deg", "\033[91mNot available\033[0m"))
            print("\033[94m\tGust:\033[0m", wind.get("gust", "\033[91mNot available\033[0m"))
        else:
            print("\033[91mWind Information: Not available\033[0m")

        if "clouds" in dict_data:
            print("\033[92mCloudiness:\033[0m", dict_data["clouds"].get("all", "\033[91mNot available\033[0m"))
        else:
            print("\033[91mCloudiness: Not available\033[0m")

        if "sys" in dict_data:
            print("\033[92mSystem Information:\033[0m")
            sys = dict_data["sys"]
            print("\033[94m\tCountry:\033[0m", sys.get("country", "\033[91mNot available\033[0m"))
            print("\033[94m\tSunrise:\033[0m", sys.get("sunrise", "\033[91mNot available\033[0m"))
            print("\033[94m\tSunset:\033[0m", sys.get("sunset", "\033[91mNot available\033[0m"))
        else:
            print("\033[91mSystem Information: Not available\033[0m")

        print("\033[92mVisibility:\033[0m", dict_data.get("visibility", "\033[91mNot available\033[0m"))
        print("\033[92mTimestamp:\033[0m", dict_data.get("dt", "\033[91mNot available\033[0m"))
        print("\033[92mTimezone:\033[0m", dict_data.get("timezone", "\033[91mNot available\033[0m"))

    except Exception as e:
        print("\033[91mAn error occurred:\033[0m", str(e))

def fetch_climate(city_name):
    """
    This function fetches the data from weather API
    with the help of City name and API Key

    input : City Name as String

    output : if Data exists : Prints data and returns true
           : else : returns false
    """
    url = "https://api.openweathermap.org/data/2.5/forecast/daily?q="+city_name+"&appid="+APIKEY+"&cnt=5"

    response = requests.request("GET", url)     # Fetch Data from API
    if(response.status_code in [200, 201]):
        print_weather_data(response.json())
        return True
    print("\033[91mThe City Name :\033[0m", city_name, "\033[91mis Incorrect. Please Retry\033[0m")
    return False

place = input("\033[92mEnter Your Location : \033[0m")
fetch_climate(place)
