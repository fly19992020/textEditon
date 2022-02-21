import random
num = random.randint()
while True:
    g = input("Please enter your guess>>")
    if g == "names":
        print("maker：fly19992020(fly19992020@outlook.com)")
    else:
        g = int(g)
    if g == num:
        print("Guess right.")
        break
    elif g < num:
        print("Too small!")
    elif g > num:
        print("Too big!")
