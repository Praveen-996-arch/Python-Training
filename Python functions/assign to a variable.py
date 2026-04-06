def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

Operations_list = {}
Operations_list["+"] = add(1,2)
Operations_list["-"] = subtract(4,3)
Operations_list["*"] = multiply
Operations_list["/"] = divide(9,3)
print(Operations_list)

print(Operations_list["*"](4,8))





