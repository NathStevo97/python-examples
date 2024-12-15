import random

positions = ["rock", "paper", "scissors"]
compPos = positions[random.randint(0, 2)]

gameActive = True

while gameActive == True:
    p1Pos = input("\n rock, paper, or scissors? ")
    if p1Pos == compPos:
        print("\n It's a tie!")
    elif p1Pos == "rock":
        if compPos == "paper":
            print("\n You Lose! Paper Covers Rock!")
        else:
            print("You Win! Rock Breaks Scissors!")
    elif p1Pos == "scissors":
        if compPos == "rock":
            print("\n You Lose! Rock Breaks Scissors!")
        else:
            print("You Win! Scissors Cuts Paper!")
    elif p1Pos == "paper":
        if compPos == "scissors":
            print("\n You Lose! Scissors Cuts Paper!")
        else:
            print("You Win! Paper Covers Rock!")

    playAgain = str(input("\n Would You Like to Play Again? Y or N? "))
    if playAgain == "Y":
        continue
    else:
        gameActive == False
    compPos = positions[random.randint(0, 2)]
