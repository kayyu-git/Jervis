import pywapi

import requests, json

from GreyMatter.SenseCells.tts import tts

#openweatherapi key
api_key = "bac947f502fc44cfc17316e02a01187b"
# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"

#openweather api city information
location = {"id": 5327684,
    "name": "Berkeley",
    "state": "CA",
    "country": "US",
    "coord": {
      "lon": -122.272751,
      "lat": 37.87159
    }
}

def weather(city_name, city_code):
	#complete_url variable to store
	#complete url address
	complete_url = base_url + "id=" + str(city_code) + "&appid=" + api_key
	#get method of requests module
	#return response object
	response = requests.get(complete_url)
	#json method of response object
	#convert json format data into python format data
	x = response.json()
	#Now x contains list of nested dictionaries 
	#Check the value of "cod" key is equal to 
	#"404", means city is found otherwise, 
	#city is not found 
	if x["cod"] != "404":
		#store the value of "main" 
		#key in variable y 
		y = x["main"]
		#store the value corresponding to the "temp" key of y (in Kelvin)
		current_temperature = int(y["temp"])
		#store the value of "weather"
		#key in variable z
		z = x["weather"]
		#store the value corresponding to the "description" key at 0 index of z
		weather_description = z[0]["description"]
		weather_result = "It is " + str(weather_description) + " in " + city_name + " with a temperature of " + str(round(current_temperature - 273.15, 1)) + " degrees Celsius or " + str(round((current_temperature - 273.15) * 9 / 5 + 32, 1)) + " degrees stupid"
		tts(weather_result)
	else:
		tts("Error accessing open weather a p i")