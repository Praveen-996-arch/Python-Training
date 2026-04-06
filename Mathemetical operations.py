# print("My age: " + str(30))
# print(123 + 456)
# print(3-2)
# print(3*2)
# print(6/3)# it returns the value in float, due to implicit type casting
# print(6//3)# it returns the int value, removes the numbers after decimals
# print(2**2)#** is exponential form
#
# ##order of operations execution - PEMDASLR
#
# print(3 *3 + 3 /3 - 3)
# # print(3 * 3 - 3 / 3 + 3)
# print(3 + 3 - 3 / 3 * 3)
#print(3 *(3 + 3) /3 - 3)

height = 1.65
weight = 84

bmi = weight / (height ** 2)
print(bmi)
print(round(bmi))## round of the entire value based on the first decimal value
print(round(bmi, 2)) ## round of the value to 2 decimals
print(round(5.789,2))