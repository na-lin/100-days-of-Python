import datetime

# # 01/04/2022
# today = datetime.datetime.now()
# print(today)
# print(today.year)
# print(today.month)
# print(today.day)
# # tomorrow = datetime.datetime(year=today.year,month=today.month,day=today.day+1)
# print(today.strftime("%d/%m/%Y"))
# tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%d/%m/%Y")
# print((datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%d/%m/%Y"))
# print(type(tomorrow))

data = {
    "users": [
        {
            "firstName": "elena",
            "lastName": "lin",
            "email": "lna483018@gmail.com",
            "id": 2
        },
        {
            "firstName": "joson",
            "lastName": "li",
            "email": "1223",
            "id": 3
        }
    ]
}

new_data = [item["email"] for item in data["users"]]
