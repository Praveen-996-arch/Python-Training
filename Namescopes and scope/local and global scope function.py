"""The above function is defined as global scope"""
def main():
    """The above function is defined as local scope"""
    def my_function():
        healthy_potion = 4
        return healthy_potion
    print(my_function())

print(main())
