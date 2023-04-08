import requests
from flight_data import FlightData
from pprint import pprint
import os

API_KEY = "ellwMlAdmXDiSnuEH41dnSxSLvXWZyIC"

URL = "https://tequila-api.kiwi.com/v2/search"
API_KEY_SEARCH = "ellwMlAdmXDiSnuEH41dnSxSLvXWZyIC"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass

    def get_iatacode(self, city_name: str):
        url = "https://tequila-api.kiwi.com/locations/query"
        headers = {
            "apikey": API_KEY,
        }
        query = {
            "term": city_name,
            "location_types": "city",
        }
        response = requests.get(url=url, params=query, headers=headers)
        response.raise_for_status()
        code = response.json()["locations"][0]["code"]
        return code

    def get_flight_price(self, original_city_code, destination_city_code, date_from, data_to):
        header = {
            "apikey": API_KEY_SEARCH,
        }
        query = {
            "fly_from": original_city_code,
            "fly_to": destination_city_code,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": data_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 30,
            "flight_type": "round",
            "one_for_city": 1,
            "only_working_days": False,
            "only_weekends": False,
            "curr": "USD",
            "max_stopovers": 0,
        }
        response = requests.get(url=URL, params=query, headers=header)
        response.raise_for_status()

        try:
            data = response.json()["data"][0]
            print("There is no direct flight to destination city.")
        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(url=URL, params=query, headers=header)
            try:
                data = response.json()["data"][0]
            except IndexError:
                return None
            else:
                flight_data = FlightData(price=data["price"],
                                         origin_city=data["route"][0]["cityFrom"],
                                         origin_airport=data["route"][0]["flyFrom"],
                                         destination_city=data["route"][1]["cityTo"],
                                         destination_airport=data["route"][1]["flyTo"],
                                         out_date=data["route"][0]["local_departure"].split("T")[0],
                                         return_date=data["route"][2]["local_departure"].split("T")[0],
                                         stop_overs=1,
                                         via_city=data["route"][0]["cityTo"]
                                         )

                return flight_data
        else:
            flight_data = FlightData(price=data["price"],
                                     origin_city=data["route"][0]["cityFrom"],
                                     origin_airport=data["route"][0]["flyFrom"],
                                     destination_city=data["route"][0]["cityTo"],
                                     destination_airport=data["route"][0]["flyTo"],
                                     out_date=data["route"][0]["local_departure"].split("T")[0],
                                     return_date=data["route"][1]["local_departure"].split("T")[0]
                                     )

            return flight_data
