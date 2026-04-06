states_of_us=["AL","OH","AK","CO","MI"]
print(states_of_us[-1])
states_of_us[1]= "Ohio"
print(states_of_us)
#append(): can add only one item to the list and at the end
states_of_us.append("New Mexico")
#extend(): adds multiple items to the list from the last
states_of_us.extend(["venezeula","alaska"])
print(states_of_us)
states_of_us.insert(1,"green")
print(states_of_us)
print(len(states_of_us)-1)

