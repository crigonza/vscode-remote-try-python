#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

def rps(score, comp_score):
    import random
    print("Welcome to Rock, Paper, Scissors!")
    print("Please choose one of the following:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    user = int(input("Enter your choice: "))
    comp = random.randint(1,3)
    if user == 1:
        print("You chose Rock")
    elif user == 2:
        print("You chose Paper")
    elif user == 3:
        print("You chose Scissors")
    else:
        print("Invalid choice")
    if comp == 1:
        print("Computer chose Rock")
    elif comp == 2:
        print("Computer chose Paper")
    elif comp == 3: 
        print("Computer chose Scissors")
    if user == comp:
        print("It's a tie!")
    elif user == 1 and comp == 2:
        print("Paper covers Rock. You lose!")
        comp_score += 1
    elif user == 1 and comp == 3:
        print("Rock smashes Scissors. You win!")
        score += 1
    elif user == 2 and comp == 1:
        print("Paper covers Rock. You win!")
        score += 1
    elif user == 2 and comp == 3:
        print("Scissors cut Paper. You lose!")
        comp_score += 1
    elif user == 3 and comp == 1:
        print("Rock smashes Scissors. You lose!")
        comp_score += 1
    elif user == 3 and comp == 2:
        print("Scissors cut Paper. You win!")
        score += 1
    else:
        print("Invalid choice")
    # print the player score and ask if they want to play again
    print("Your score is: " + str(score))
    print("The computer's score is: " + str(comp_score))

    play_again = input("Would you like to play again? (y/n): ")
    if play_again == "y":
        rps(score, comp_score)
    else:
        print("Thanks for playing!")
        exit()

#run the game
rps(0, 0)
