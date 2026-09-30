import requests
from twilio.rest import Client
import os

api_key = os.environ.get("API_KEY")

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

param = {
    "lon": os.environ.get("YOUR_LONGITUDE"),
    "lat": os.environ.get("YOUR_LATITUDE"),
    "cnt": 4,
    "appid": api_key
}

response = requests.get(url= "https://api.openweathermap.org/data/2.5/forecast", params= param)
response.raise_for_status()

weather_data = response.json()['list']

will_rain = False
for data in weather_data:
    weather_id = data['weather'][0]['id']
    if weather_id < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_=os.environ.get("FROM_PHONE_NUMBER"),
        body="It's going to rain today! Bring an umbrella. ☔",
        to=os.environ.get("TO_PHONE_NUMBER")
    )

    print(message.status)
