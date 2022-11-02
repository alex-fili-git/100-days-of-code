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

import pandas as pd
data = pd.read_csv("weather_data.csv")
print(data["temp"])
