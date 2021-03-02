from capitals import states
# PSEUDOCODE
# * randomize the capitals array
# * display welcome message
# * interpolate state name in prompt for user input (e.g. What is the capital of _state_ ?)
# * after user input, compare user input to array value for capital
# * if user input matches array value, add 1 to "correct" score
# * if user input does not match array value, add 1 to "incorrect" score
# * prompt user if they would like to play again

import random
def play_game():
    random.shuffle(states)

    print("")
    print("Welcome to the State Capital game!")
    print("follow the prompts below...")
    print("")
    
    correct = 0
    incorrect = 0

    for state in states:
        user_input = input("What is the capital of " + states[states.index(state)]["name"] + "? ")
        if user_input == states[states.index(state)]["capital"]:
            correct = correct + 1
        else:
            incorrect = incorrect + 1
        print("")
        print("Correct: {}".format(correct))
        print("Incorrect: {}".format(incorrect))
        print("")
    print("")
    print("Game Over!")
    print("Your final score was {}".format(correct) + " correct, and {}".format(incorrect) + " incorrect!")
    print("")

play_game()

play_again = "y"

while play_again == "y":
    play_again = input("Would you like to play again? [y,n] ")
    print("")
    if play_again == "y":
        play_game()
    elif play_again == "n":
        print("thanks for playing!")
    else:
        print("invalid command, exiting game")