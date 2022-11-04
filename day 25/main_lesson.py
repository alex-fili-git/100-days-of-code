# with open("weather_data.csv") as data_file:
#     data = data_file
#     print(data.readlines())

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data[1:]:
#         temperatures.append(int(row[1]))
# Too much faff here ^^, so we want help from pandas library

# import pandas as pd
# data = pd.read_csv("weather_data.csv")
# print(data["temp"].max())

import pandas as pd
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")["Primary Fur Color"]
new_data = {"Fur Color": ["grey", "red", "black"], "Count": [data.value_counts()[0], data.value_counts()[1], data.value_counts()[2]]}
data_squirrel = pd.DataFrame(new_data)
data_squirrel.to_csv("squirrel_count.csv")

