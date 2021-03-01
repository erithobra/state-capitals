from capitals import states
# PSEUDOCODE
# * randomize the capitals array
# * display welcome message
# interpolate state name in prompt for user input (e.g. What is the capital of _state_ ?)
# after user input, compare user input to array value for capital
# if user input matches array value, add 1 to "correct" score
# if user input does not match array value, add 1 to "incorrect" score
# prompt user if they would like to play again

import random
random.shuffle(states)

print("Welcome to the State Capital game!")
print("follow the prompts below...")

correct = 0
incorrect = 0

for state in states:

    print(states[states.index(state)]["name"])

    user_input = input("What is the capital of " + states[states.index(state)]["name"] + "? ")

    if user_input == states[states.index(state)]["capital"]:
        correct = correct + 1
        print("here")
    else:
        incorrect = incorrect + 1
        print("no, here")

    print("Correct: {}".format(correct))
    print("Incorrect: {}".format(incorrect))


print("Game Over!")
print("Your final score was {}".format(correct) + " correct, and {}".format(incorrect) + " incorrect!")