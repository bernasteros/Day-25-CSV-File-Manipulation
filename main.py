import pandas

# Simply read the file with pandas
data = pandas.read_csv("weather_data.csv")

# Cool feature: convert the csv into other types (e.g. python-readable dict)
data_dict = data.to_dict()
print(data_dict)

# Cherry-Picking: extract a list for a specific element
temp_list = data["temp"].to_list()
print(temp_list)

average_temp = data["temp"].mean()
median_temp = data["temp"].median()
max_temp = data["temp"].max()
print(f"The average temperature is {round(average_temp, 2)}°C\n"
      f"The median is {median_temp}°C\n"
      f"The maximum temperature is {max_temp}°C")

# Get Data in Row
print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]
print(monday.condition)

mtemp = (monday.temp * 9/5) + 32
print(monday.temp)
print(mtemp)
