import requests
import json


city_name = "Helsinki"
API_key = "408d42c214db9b831bf183f48da10355"
suomeksi = "&units=matric"

def get_weather():
    # HTTP GET https://api.tvmaze.com/search/shows?q=emmerdale
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}{suomeksi}"
    # Käsitellään mahdolliset virheet verkkoyhteydessä.
    response = requests.get(url)
    response_body = response.json()


    print(json.dumps(response_body, indent=2))
    lampotila = response_body["main"]['temp']
    print(f"lampotila nyt Henlsingissä on: {lampotila} astetta")
    kuvaus = response_body['weather'][0]['description']
    print(kuvaus)

get_weather()



