import requests

GET_URL = "https://api.sheety.co/f4a833d9ad7aed79786c4ac0d41236ac/flightDeals/prices"
USER_POST_URL = "https://api.sheety.co/f4a833d9ad7aed79786c4ac0d41236ac/flightDeals/users"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass

    def get_destination_data(self):
        response = requests.get(url=GET_URL)
        response.raise_for_status()
        data = response.json()
        destination_data = data["prices"]
        return destination_data

    def update_data(self, update_data: str, id: str):
        post_url = f"{GET_URL}/{id}"
        # NEW: print response.text before raise exception to get more details about error.
        new_data = {
            "price": {
                "iataCode": update_data,
            }
        }
        put_response = requests.put(url=post_url, json=new_data)
        put_response.raise_for_status()

    def post_user_data(self, first_name, last_name, email):
        body = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
            }
        }
        post_response = requests.post(url=USER_POST_URL, json=body)
        print(post_response.content)
        print(post_response.text)
        post_response.raise_for_status()

    def get_user_data(self):
        response = requests.get(url="https://api.sheety.co/f4a833d9ad7aed79786c4ac0d41236ac/flightDeals/users")
        response.raise_for_status()
        data = response.json()

        return data
