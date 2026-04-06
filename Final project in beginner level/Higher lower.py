

Brand = {
    "Ariana Grande, a Musician and actress, from United States" : 245678,
    "Victoria's secret, a lingerie brand, from United States" : 245679,
    "Maluma,a a Musician, from Columbia" : 12344,
    "Kendall Jenner, a reality TV personality and Model, from United States":34648

}
i=0
j=0
Current_score = 0
Final_score = 1
def compare(A_value, B_value):
    user_input = input("Who has more followers? Type 'A' or 'B': ").upper()
    global Current_score
    global Final_score
    if A_value < B_value and user_input == 'A':
        print(f"Sorry, that's wrong. Final score: {Current_score}")
        Current_score -=1
        return True
    elif A_value < B_value and user_input == 'B':
        Current_score += 1
        print(f"You are right, Current score: {Current_score}")
    elif A_value > B_value and user_input == 'A':
        Current_score += 1
        print(f"You are right, Current score: {Current_score}")
    elif A_value > B_value and user_input == 'B':
        print(f"Sorry, that's wrong. Final score: {Current_score}")
        Current_score += 1
        return True
    Final_score += 1

def higher_lower():
    global i
    global j
    for key, value in Brand.items():
        list_of_keys = list(Brand.keys())
        list_of_values = list(Brand.values())
        if i == 0:
            A = list_of_values[j]
            print(f"Compare A: {list_of_keys[j]}")
            print("Versus")
        elif i == 1:
            B = list_of_values[j]
            print(f"Against B: {list_of_keys[j]}")
        i+=1
        j +=1
        if i >=2:
         break
    compare(A,B)
    if Final_score == 1:
        exit
    elif Final_score == Current_score:
        exit
    elif Final_score > Current_score:
        i = 0
        j -= 1
        higher_lower()

higher_lower()




