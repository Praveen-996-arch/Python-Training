capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
#List in dictionary
travel_log = {
    "France": ["Paris", "lille", "Dijon"],
    "Germany": ["Berlin", "Stuttgart"]
}

# print(travel_log["France"][1])
#Nested list
nested_list = ["A", "B", ["C", "D"]]
#print(nested_list[2][1])

#Nested dictionary
travel_log = {
    "France": ["Paris", "lille", "Dijon"],
    "Germany": ["Berlin", "Stuttgart"],
    "capital": {
    "France": "Paris",
    "Germany": "Berlin",
}}
print(travel_log["capital"]["France"])