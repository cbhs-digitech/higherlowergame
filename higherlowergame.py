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

# Set lives to 5

# Set score to 0

# Generate random number for user to guess (answer)

# While lives > 0 keep playing

   # Get user guess
   user_guess = int(input("Please enter a number between 1 and 10 inclusive: "))
   # if user guess == answer

      # Update Score

      # Update lives
      
   # else if user guess < answer

      # too low
      # lose a life and display message
   # else if user guess > answer

      # too high
      # lose a life and display message

# when out of lives (end of while loop) display game over message
# display final score
