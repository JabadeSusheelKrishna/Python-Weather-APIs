import requests

API_Key = "07e213c2132eda0e9013476bed601071"

def print_weather_data(Dict_Data):
    try:
        if "name" in Dict_Data:
            print("Location:", Dict_Data["name"])
        else:
            print("Location: Not available")

        if "coord" in Dict_Data:
            print("Coordinates:")
            if "lat" in Dict_Data["coord"]:
                print("\tLatitude:", Dict_Data["coord"]["lat"])
            else:
                print("\tLatitude: Not available")
            if "lon" in Dict_Data["coord"]:
                print("\tLongitude:", Dict_Data["coord"]["lon"])
            else:
                print("\tLongitude: Not available")
        else:
            print("Coordinates: Not available")

        if "weather" in Dict_Data and len(Dict_Data["weather"]) > 0:
            print("Weather Conditions:")
            weather = Dict_Data["weather"][0]
            if "main" in weather:
                print("\tNature:", weather["main"], "(", weather.get("description", "Description not available"), ")")
            else:
                print("\tNature: Not available")
        else:
            print("Weather Conditions: Not available")

        if "main" in Dict_Data:
            print("Temperature Information:")
            main = Dict_Data["main"]
            print("\tTemperature:", main.get("temp", "Not available"))
            print("\tFeels Like:", main.get("feels_like", "Not available"))
            print("\tMinimum Temperature:", main.get("temp_min", "Not available"))
            print("\tMaximum Temperature:", main.get("temp_max", "Not available"))
            print("\tPressure:", main.get("pressure", "Not available"))
            print("\tHumidity:", main.get("humidity", "Not available"))
        else:
            print("Temperature Information: Not available")

        if "wind" in Dict_Data:
            print("Wind Information:")
            wind = Dict_Data["wind"]
            print("\tSpeed:", wind.get("speed", "Not available"))
            print("\tDirection:", wind.get("deg", "Not available"))
            print("\tGust:", wind.get("gust", "Not available"))
        else:
            print("Wind Information: Not available")

        if "clouds" in Dict_Data:
            print("Cloudiness:", Dict_Data["clouds"].get("all", "Not available"))
        else:
            print("Cloudiness: Not available")

        if "sys" in Dict_Data:
            print("System Information:")
            sys = Dict_Data["sys"]
            print("\tCountry:", sys.get("country", "Not available"))
            print("\tSunrise:", sys.get("sunrise", "Not available"))
            print("\tSunset:", sys.get("sunset", "Not available"))
        else:
            print("System Information: Not available")

        print("Visibility:", Dict_Data.get("visibility", "Not available"))
        print("Timestamp:", Dict_Data.get("dt", "Not available"))
        print("Timezone:", Dict_Data.get("timezone", "Not available"))

    except Exception as e:
        print("An error occurred:", str(e))

def Fetch_Climate(city_name):
    url = "https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid="+API_Key

    response = requests.request("GET", url)
    if(response.status_code in [200, 201]):
        print_weather_data(response.json())
        return True
    else:
        print("The City Name : ", city_name, " Incorrect. Please Retry")
        return False
    

place = input("Enter Your Location : ")
Fetch_Climate(place)