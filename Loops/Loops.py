#for loop
from operator import add

# fruits = ["apple","banana","orange"]
# for fruit in fruits:
#     print(fruit)
#     print(fruits)
#     print(fruit + "pie")
# print(fruits)

#Adding all the numbers in the list
# groceries_item_individual_price=[21,34,56,23,34,5,6,7,8,12,3]
# sum = 0
# for item in groceries_item_individual_price:
#     sum += item
# print(sum)

# find maximum number in the list
groceries_item_individual_price=[21,34,56,23,34,5,6,7,8,12,3]


max_score=0
for item in groceries_item_individual_price:
    if item > max_score:
        max_score = item
print(max_score)
