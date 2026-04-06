

import pandas

data = pandas.read_csv("/Users/manasapola/PycharmProjects/Basicsofpython/readdatafromcsv/weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# # print(data_dict)
# temp_list = data["temp"].tolist()
# print(temp_list)
# # sum = sum(temp_list)
# # total = len(temp_list)
# # average = sum / total
# # print(average)

# mean =data["temp"].mean()
# print(mean)
# max_temp = data.temp.max()
# # print(max)
# # getting a paeticular row data
# print(data[data.temp < max_temp])
mondaydata = data[data.day == "Monday"]
print(mondaydata.condition)
mon_temp = mondaydata.temp.iloc[0]
print(mon_temp)
mon_temp_f = mon_temp * 9/5 + 32
print(f"Temperature in Fahrenheit: {mon_temp_f}")