import csv

with open("./weather_data.csv", mode="r") as data_file:
    data = csv.reader(data_file)

    for row in data:
        print(row)
