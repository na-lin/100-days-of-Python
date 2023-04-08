import requests
def create_account(USER_NAME, USER_TOKEN):
    pixela_endpoint = "https://pixe.la/v1/users"
    user_params = {
        "token": USER_TOKEN,
        "username": USER_NAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    create_response = requests.post(url=pixela_endpoint, json=user_params)
    print(create_response.text)

