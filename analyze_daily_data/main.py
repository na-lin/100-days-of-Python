import pandas
import json
index_range = []
for _ in range(0,56):
    index_range.append(_)
# print(index_range)
original_data = pandas.read_csv("./data/report.csv")
new_data = original_data.reindex(index=original_data.index[::-1])
print(new_data)
# # new_data.to_json("./data/fix.json")
# new_data.reindex(index=[0:55:-1])
new_data.to_csv("./data/fix.csv")

# print(original_data)

