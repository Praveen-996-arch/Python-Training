import pandas as pd
new_DF = pd.DataFrame({"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]})
new_DF.to_csv("/Users/manasapola/PycharmProjects/Basicsofpython/readdatafromcsv/new_csv.csv", index=False)  # index=False is used to avoid writing the index column to the CSV file. By default, when you create a DataFrame and save it to a CSV file, pandas includes an index column that assigns a unique identifier to each row. Setting index=False prevents this index column from being written to the CSV file, resulting in a cleaner and more straightforward CSV output that only contains the actual data without any additional indexing information.
with open("/Users/manasapola/PycharmProjects/Basicsofpython/readdatafromcsv/new_csv.csv") as data_file:
    data = data_file.read()
    print(data)