import requests

API_key = ""

parameters = {
    "appid": API_key,
    "q": "Venice,IT"
}

response = requests.get("http://api.openweathermap.org/data/3.0/weather", params=parameters)
response.raise_for_status()
weather_data = response.json()
if weather_data["weather"][0]["id"] <700:
    print("bring umbrella")
 
