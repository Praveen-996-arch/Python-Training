potion_health = 2
"""The above variable is defined as global scope"""

def my_function():
    healthy_potion = 4
    """The above variable is defined as local scope"""
    return potion_health, healthy_potion

print(my_function())
