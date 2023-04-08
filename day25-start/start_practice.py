# TODO 1: open weather_date.csv.readlines() to create a list named data that contains the value from the .csv file

# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# NEW: to fass to get a column data with so many lines of code
# import csv
#
# with open("weather_data.csv") as weather_date:
#     data = csv.reader(weather_date)
#     # print(data)
#     temperature = []
#     for row in data:
#         # print(row)
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

# New: open & read
data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# temp_list = data["temp"].tolist()
# # print(new_temp)
# # NEW: average = mean
# # average_temp = round(sum(temp_list) / len(temp_list))
# # print(average_temp)
# print(data["temp"].mean())
# print(data["temp"].max())

# NEW: GET DATA in columns

# NEW :GET DATA IN ROW
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
# print(monday)
# print(monday.condition)
# C *1.8 + 32 = F
print(int(monday.temp) * 1.8 + 32)
print(monday.temp * 1.8 + 32)
print(type(data.temp))
# print(type(monday.temp))

# TODO: create a dataframe
data_dict = {
    "student": ["angela", "lin"],
    "score": [88, 90]
}
data = pandas.DataFrame(data_dict)
data.to_csv("student_score.csv")
