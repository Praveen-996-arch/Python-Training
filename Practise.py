user_input = int(input("Please enter a number:"))
i = 1

# sum = 0
#
#
#
# while i <= user_input:
#     sum += i
#     i +=1
#
# print(sum)

while i <= user_input:
    if user_input % i == 0:
        print(i)
    i +=1