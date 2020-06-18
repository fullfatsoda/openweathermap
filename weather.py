# get the current weather for your city using api.openweathermap.org
# you will need an api key which you can get for free

import requests

city_name   = '' # name of the city
country     = '' # use ISO 3166 country code e.g. GB
api_key     = '' # enter your api key here

# connect to the api
get_weather = requests.get(
    'https://api.openweathermap.org/data/2.5/weather?q='
    + city_name
    + ','
    + country
    + '&appid='
    + api_key
    )
# get the data in .json format
get_weather_json = get_weather.json()

# return the data

# description of the weather today
description = get_weather_json['weather'][0]['description']

# temperature in celcius to 1 decimal place
kelvin      = 273 # api temperatures are in kelvin (-273 to get celcius)
temperature = round(((get_weather_json['main']['temp']) - kelvin), 1)
feels_like  = round(((get_weather_json['main']['feels_like']) - kelvin), 1)

# pressure and humidity
pressure    = get_weather_json['main']['pressure']
humidity    = get_weather_json['main']['humidity']

# wind speed - defauts to metres per second and degrees
# converted to miles per hour and compass direction
mph         = 2.2369 # mulitply by mph to convert from metres per second
            # round wind speed to one decimal place
wind_speed  = round(get_weather_json['wind']['speed'] * mph, 1)
wind_degree = get_weather_json['wind']['deg']

# change from degree to compass direction
def degree_to_direction(degree):
    # compass directions change for every 22.5 degrees
    # adding 0.5 is to ensure the value can't be equal to two directions
    value       = int((degree / 22.5) + 0.5)
    directions  = [
                "N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW",
                ]
    return directions[(value % 16)] # 16 directions

# rain fallen in the past hour (mm) and cloud coverage as a %
try: # if there is any rain
    rain = get_weather_json['rain']['1h']
except:
    rain = 0 # there is no rain

clouds  = get_weather_json['clouds']['all']

# display the information in a readable format
print(f"Weather for {city_name}\nToday there will be {description}")
print(f"Current temperature is {temperature} C but will feel like {feels_like} C")
print(f"Atmospheric pressure {pressure} - Humidity {humidity}%")
print(f"Wind speed {wind_speed}mph coming from {degree_to_direction(wind_degree)}")
print(f"{rain}mm of rain fallen in the last hour and {clouds}% cloud coverage")
