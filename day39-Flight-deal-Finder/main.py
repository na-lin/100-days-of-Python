# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from get_user_information import GetUserInfor
from datetime import datetime, timedelta

ORIGINAL_CITY_CODE = "NYC"

# get_user_information = GetUserInfor()
data_manager = DataManager()
flight_search = FlightSearch()


# get user information and post into google sheet
# first_name = get_user_information.first_name
# last_name = get_user_information.last_name
# email = get_user_information.email
# data_manager.post_user_data(first_name, last_name, email)

tomorrow = datetime.now() + timedelta(days=1)
six_month = datetime.now() + timedelta(days=180)

sheet_data = data_manager.get_destination_data()
for city_data in sheet_data:
    # if miss IATA, call API to get IATA of city
    if len(city_data["iataCode"]) == 0:
        city_data["iataCode"] = flight_search.get_iatacode(city_name=city_data["city"])
        data_manager.update_data(city_data["iataCode"], city_data["id"])

    # get cheapest price

    flight = flight_search.get_flight_price(original_city_code=ORIGINAL_CITY_CODE,
                                            destination_city_code=city_data["iataCode"],
                                            date_from=tomorrow,
                                            data_to=six_month
                                            )
    if flight is None:
        print(f"{city_data['city']} Current flight is not exist,"
              f"the lowest Price You want is {city_data['lowestPrice']}\n")
        continue

    if flight.price < city_data["lowestPrice"]:
        user_email = [item["email"] for item in data_manager.get_user_data()["users"]]
        user_name = [item["firstName"] for item in data_manager.get_user_data()["users"]]

        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over , via {flight.via_city}."

        notification = NotificationManager(message)
        notification.send_sms()

        notification.send_email(to_address=user_email, message=message)



    else:
        print(f"{city_data['city']} Current price is not exist,"
              f"the lowest Price You want is {city_data['lowestPrice']}")
