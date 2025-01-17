# Importing the random module to generate random numbers
import random

# Defining the user_guess function
def user_guess():
    # Generating a random number between 1 and 10 (inclusive)
    computer_number = random.randint(1, 10)

    # Starting a while loop to keep asking for guesses until the correct number is guessed
    while True:
        # Asking the user to enter a number between 1 and 10
        n = int(input("Enter number between 1 to 10: "))
        
        # If the user enters a non-positive number, ask them to enter a positive number
        if n <= 0:
            print("Enter a positive number")
        
        # If the user's guess matches the computer's number, they win
        elif n == computer_number:
            print("Your guess is right!")
            break  # Exit the loop once the correct guess is made
        
        # If the user's guess is greater than the computer's number, they are asked to try a smaller number
        elif n > computer_number:
            print("Your number is higher, try another number")
        
        # If the user's guess is smaller than the computer's number, they are asked to try a larger number
        elif n < computer_number:
            print("Your number is smaller, try another number")
        
        # If the user enters an invalid number (which shouldn't happen because we convert to int), ask them to try again
        else:
            print("Invalid number, try another number")

# Calling the user_guess function to start the game
user_guess()
