import requests


response = requests.get("https://api.chucknorris.io/jokes/random")
response_body = response.json()
print(response_body)

for item in response_body:
    print(item['jokes'])
    print(type(item['jokes']))