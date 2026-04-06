print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
direction=input("Do you want to go left or right?")
if direction.lower() == 'left':
    action = input("Do you want to swim or wait?")
    if action.lower() == 'wait':
        color=input("Do you want to go to which color door?")
        if color.lower() == 'yellow':
            print("You Win!")
        elif color.lower() == 'Blue' or color == 'Red':
            print("Game Over")
    elif action.lower() == 'swim':
        print("Game Over")
elif direction.lower() == 'right':
    print("Game Over")