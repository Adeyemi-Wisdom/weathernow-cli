import requests
key = "437ed221b19a64d4c6d18cc4d3a0f796"
url = "https://api.openweathermap.org/data/2.5/weather"
state = input("Enter Your Geo_Location: ")
params = {
    "q": state,
    "appid": key,
    "units": "metric"
}
response = requests.get(url, params= params)
if response.status_code == 200:
    data = response.json()
    description =    data['weather'][0]['description']
    temp = data['main']['temp']
    print(f"Weather Information: {description}, {temp}°C")
else:
    print(f"Error {response.status_code}: {response.text}")
