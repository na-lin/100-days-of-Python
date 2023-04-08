import requests
from datetime import datetime
import os
BORN_YEAR = 1998
WEIGHT_KG = 49
HEIGHT_CM = 161

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ["API_KEY"]
EXECISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = "https://api.sheety.co/f4a833d9ad7aed79786c4ac0d41236ac/workoutTracker/workouts"
header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_parmas = {
    "query": input("What exercise do you have done today?"),
    "gender": "female",
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": datetime.now().year - BORN_YEAR
}
exerices_response = requests.post(url=EXECISE_ENDPOINT,json=exercise_parmas,headers=header)
data = exerices_response.json()
print(data)
token = "fdsjlkfjlsjfldsjlfs"
for exercise in data["exercises"]:
    sheet_header = {
        "Authorization": "Bearer fdsjlkfjlsjfldsjlfs",
    }
    exercise_data = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheet_response = requests.post(url=EXECISE_ENDPOINT, json=exercise_data, headers=sheet_header)
    print(sheet_response.text)
    print(sheet_response.status_code)
    print(sheet_response.content)
    sheet_response.raise_for_status()
# ran 2 hours and walk 1 hours