#add function with variable number of arguments
#these variables are called as *args, it is a tuple

# def add(*num):
#     total = 0
#     for n in num: 
#         # print(n)
#         total += n
#     print(total)
#     print(num[3])

# add(1,2,3,4.5,7,8)

#keyword arguments, these are called as **kwargs, it is a dictionary



# def calculate(n,**args):
    
#     n += args['add']
#     n += args['multiply']
#     print(n)
# calculate(2, add = 2, multiply = 3)

class Car:
    def __init__(self,**kw):
        self.make = kw['make']
        self.model = kw['model']
        self.year = kw.get('year') #if year is not provided, it will return None instead of throwing an error
        print(self.make, self.model)
my_car = Car(make = 'Nissan', model = 'GT-R')