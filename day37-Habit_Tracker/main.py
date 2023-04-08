import requests
from datetime import datetime
USER_NAME = "elena2022"
USER_TOKEN = "Elena_habit_create_my_self"
GRAPH_ID = "graph1"
# ADD data
ADD_DATE = "20220210"
ADD_QUANTITY = "200"
# update data
UPDATE_DAY = 20220211
UPDATE_DATA = "208"
# delete data
DELETE_DATE = 20220214
# TODO : step 1 create account
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": USER_TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# create_response = requests.post(url=user_endpoint, json=user_params)
# print(create_response.text)


# TODO 2: step 2: create a graph
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
graph_params = {
    "id": GRAPH_ID,
    "name": "Coding Time",
    "unit": "minute",
    "type": "int",
    "color": "ajisai",
}
graph_authenticate = {
    "X-USER-TOKEN": USER_TOKEN,
}
graph_response = requests.post(url=graph_endpoint,json=graph_params, headers=graph_authenticate)
# print(graph_response.text)


# TODO 3: post data into graph
today = datetime.now()
quantity_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
quantity_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many quantity do you want to input:"),
}
quantity_response = requests.post(url=quantity_endpoint, json=quantity_params, headers=graph_authenticate)
print(quantity_response.text)

# TODO 4: update data
# endppoint /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>

update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{UPDATE_DAY}"
update_data = {
    "quantity": UPDATE_DATA,
}
# update_response = requests.put(url=update_endpoint, json=update_data, headers=graph_authenticate)
# print(update_response.text)

# TODO 5: delete request
# delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{DELETE_DATE}"
# delete_response = requests.delete(url=delete_endpoint, headers=graph_authenticate)
# print(delete_response.text)

