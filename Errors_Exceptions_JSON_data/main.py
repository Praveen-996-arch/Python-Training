#File not found error
a_dict = {"key":"value"}
try:
    file = open("/Users/manasapola/PycharmProjects/Basicsofpython/Errors_Exceptions_JSON_data/a_file.txt")
    content = file.read()
    print(content)
    print(a_dict)
    
except FileNotFoundError:
    file = open("/Users/manasapola/PycharmProjects/Basicsofpython/Errors_Exceptions_JSON_data/a_file.txt", mode= 'w')
    file.write("Hello World")
except KeyError:
    a_dict["add"] = "sum"
    print(a_dict['add'])
else:
    file =  open("/Users/manasapola/PycharmProjects/Basicsofpython/Errors_Exceptions_JSON_data/a_file.txt", mode= 'a')
    file.write("\nHow are you")
finally:
    file.close()
    print("File was closed.")


    
   

