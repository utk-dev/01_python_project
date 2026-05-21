'''
snake = -1
water = 1
gun = 0'''

import random
computer = random.choice([1,0,-1])

print(f"s for 🐍\nw for 💧\ng for 🔫")

youstr = input("Enter your choice: ")
youDict = {"s":-1, "w":1, "g":0}
you = youDict[youstr]
reverseDict = {-1:"Snake", 1:"Water", 0:"Gun"}

print(f"Computer chose: {reverseDict[computer]} \nYou chose: {reverseDict[you]}")

if (computer-you)==0:
    print("It's a tie!")
else:
    if (computer-you==2) or (computer-you==-1):
        print("Computer wins!")
    else:
        print("You win!")
