# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))

# print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")

# media_temp = data.temp.mean()
# max_value = data.temp.max()
# print(max_value)
# print(f"{media_temp:.2f}")

monday = data[data.day == "Monday"]

f = monday.temp * 1.8 + 32

print(str(f))

