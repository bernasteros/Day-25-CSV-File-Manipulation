import pandas

# Simply read the file with pandas
data = pandas.read_csv("weather_data.csv")

# Cool feature: convert the csv into other types (e.g. python-readable dict)
data_dict = data.to_dict()
print(data_dict)

# Cherry-Picking: extract a list for a specific element
temp_list = data["temp"].to_list()
print(temp_list)