import requests
import json

def show_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    response_body = response.json()
    print(response_body)

    joke = response_body['value']
    print(f"tässä vitsi käyttäjälle: {joke}")

show_joke()
