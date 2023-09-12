import random

# Set the range for the random number (e.g., 1 to 100)
min_number = 1
max_number = 100

# Generate a random number within the specified range
secret_number = random.randint(min_number, max_number)

# Initialize the number of attempts
attempts = 0

# Set the maximum number of attempts for the player
max_attempts = 10

print("Welcome to the Guess the Number game!")
print(f"I'm thinking of a number between {min_number} and {max_number}.")
print("Can you guess what it is?")

# Main game loop
while attempts < max_attempts:
    try:
        # Get the player's guess
        guess = int(input("Enter your guess: "))
        
        # Increment the number of attempts
        attempts += 1

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")
        
        # Check if the player has run out of attempts
        if attempts == max_attempts:
            print(f"Sorry, you've reached the maximum number of attempts. The secret number was {secret_number}.")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("Thanks for playing!")
