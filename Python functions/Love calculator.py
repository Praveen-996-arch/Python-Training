def calculate_love_score(name1, name2):
    True_word = "TRUE"
    Love_word = "LOVE"
    trueCount =0
    loveCount =0
    for letter1 in True_word.lower():
        sum=0
        for letter2 in name1:
            if letter2 == letter1:
                sum+=1
        for letter3 in name2:
            if letter3 == letter1:
                sum += 1
        trueCount = trueCount + sum
        print(f"{letter1.upper()} occurs {sum} times")
    print(f"Total={trueCount}")

    for letter1 in Love_word.lower():
        sum=0
        for letter2 in name1:
            if letter2 == letter1:
                sum+=1
        for letter3 in name2:
            if letter3 == letter1:
                sum += 1
        loveCount = loveCount + sum
        print(f"{letter1.upper()} occurs {sum} times")
    print(f"Total={loveCount}")
    print(f"Love Score == {trueCount}{loveCount}")

        #count = count + sum
        #print(count)




calculate_love_score(name1 ="Praveen",name2 = "Meena")


