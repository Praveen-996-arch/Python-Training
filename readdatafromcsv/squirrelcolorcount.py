import pandas as pd

data = pd.read_csv("/Users/manasapola/PycharmProjects/Basicsofpython/readdatafromcsv/Squirreldata.csv")
fur_color = (data["Primary Fur Color"]).tolist()
# print(fur_color)
gray = fur_color.count("Gray")
cinnamon = fur_color.count("Cinnamon")
black = fur_color.count("Black")
red = fur_color.count("Red")
# print(gray, red, black)
color_count_tb = pd.DataFrame({"Fur Color" : ["Gray", "Cinnamon" , "Black", "Red"], "Count": [gray,cinnamon,black,red]})
print(color_count_tb)
color_count_tb.to_csv("/Users/manasapola/PycharmProjects/Basicsofpython/readdatafromcsv/Squirrelcolorcount.csv")