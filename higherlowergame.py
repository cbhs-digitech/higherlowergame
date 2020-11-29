# Higher Lower Game
#
# Your task is to create a game that will randomly choose a number
# between 1 and 50 and then ask the user to guess the number.
#
# If they guess too low they will be told too low, if they guess
# too high they wil lbe told too high.
#
# The player will have five lives, for each incorrect guess they
# will loose a life.
# If they guess correct they get a point added to their score and
# five more lives
#
# 1) Complete the program
# 2) Make improvements to the program to make it more robust and efficient.

# Import random number generator
import random
# Set lives to 5
lives = 5

# Set score to 0
score = 0

# Generate random number for user to guess (answer)
answer = random.randint(1, 10)

# While lives > 0 keep playing
while lives > 0:
    # Get user guess
    user_guess = int(
        input("Please enter a number between 1 and 10 inclusive: "))
    # if user guess == answer
    if user_guess == answer:
        print("Correct, lte's go again")
        # Update Score
        score = score + 1

        # Update lives
        lives = lives + 5
        answer = random.randint(1, 10)

    # else if user guess < answer
    elif user_guess < answer:
        # too low
        print("Your guess was too low.")
        # lose a life and display message
        lives = lives - 1
    # else if user guess > answer
    elif user_guess > answer:
        # too high
        print("Your guess was too high.")
        # lose a life and display message
        lives = lives - 1

# when out of lives (end of while loop) display game over message
# display final score
print("Game over, you scored " + str(score)
