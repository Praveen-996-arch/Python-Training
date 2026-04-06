#Main class

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")

#inherited class from above class
class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.num_eyes = 3#Inheriting method from parent class
    def breathe(self):
        super().breathe()
        print("Underwater")

nemo = Fish()
nemo.breathe()
print(nemo.num_eyes)