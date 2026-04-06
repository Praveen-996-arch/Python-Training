with open("/Users/manasapola/PycharmProjects/Basicsofpython/listcomprehension/file1.txt") as file1:
    numbers = file1.readlines()
    numbers = [n.strip("\n") for n in numbers]
    print(numbers)
with open("/Users/manasapola/PycharmProjects/Basicsofpython/listcomprehension/file2.txt") as file2:
    numbers2 = file2.readlines()
    numbers2 = [n.strip("\n") for n in numbers2]
    print(numbers2)
result = [n for n in numbers if n in numbers2]
print(result)