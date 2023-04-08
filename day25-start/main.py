# import pandas
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# fur_color = data["Primary Fur Color"]
# color_count = fur_color.value_counts()
# print(color_count)
#
# squirrel_color_data = {
#     "Fur color": ["Gray", "Cinnamon", "Black"],
#     "count": [color_count[0], color_count[1], color_count[2]]
# }
# squirrel_data = pandas.DataFrame(squirrel_color_data)
# print(squirrel_data)
# squirrel_data.to_csv("squirrel_color_data.csv")

import pandas as pd
# age = pandas.Series([22,21,15],name = 'age')
# dp_age = pandas.DataFrame(age)
# print(age)
# print(dp_age)
#todo: this is a todo comment

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)
print(df.shape)