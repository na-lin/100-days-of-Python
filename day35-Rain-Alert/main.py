import requests
import os
from twilio.rest import Client
# my position: 40.708979,286.017400, 106.017400
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_parameter = {
    "lat":40.708979,
    "lon": 106.017400,
    "exclude": "current,minutely,daily",
    "appid": os.environ.get("OWN_API_KEY")
}
account_sid = 'AC533ce877dd8c0c2ed97afdf136833441'
auth_token = '9e55c738bcb90897e584c6c8311f73ec'

# API longtitude range from -180 ~ 180
response = requests.get(url=OWM_Endpoint, params=weather_parameter)
response.raise_for_status()
weather_data = response.json()
weather_condition_12hour = [item["weather"][0]["id"] for item in weather_data["hourly"][:12]]
rain_condition = [item for item in weather_condition_12hour if item < 700]
if len(rain_condition) > 0:
    # print("Bring an Umbrella")

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='There may rain in 12 hours, Please remember to Bring an Umbrella.',
        from_='+18456689981',
        to='+16463318838'
    )
    print(message.status)
