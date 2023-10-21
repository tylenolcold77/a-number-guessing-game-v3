import random
import statistics

def start_game():
    # Welcome message
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    
    high_score = [None]  # Initialize high score with positive infinity.
    
    while True:
        # Generate a random winning number
        winning_number = random.randint(1, 100)
        print(f"Can you beat the current high score of {high_score} attempts?")
        
        attempts = []  # List to store player's guess attempts

        while True:
            try:
                guess = int(input("Take a guess: "))  # Prompt the player for a guess
                if guess < 1 or guess > 100:
                    print("Your guess is outside the range of 1-100. Try again.")
                    continue  # Continue the loop if the guess is out of range
            except ValueError:
                print("Please enter a valid whole number.")
                continue  # Continue the loop if the input is not a valid integer
            
            attempts.append(guess)  # Add the guess to the list of attempts
            
            if guess < winning_number:
                print("Too low! Try a higher number.")
            elif guess > winning_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed the number in {len(attempts)} attempts!")
                if len(attempts) < len(high_score) or high_score[0] is None:
                    high_score[0] = len(attempts)
                    print(f"New high score! {len(attempts)} attempts.")
                break  # Exit the loop when the correct number is guessed
            
        play_again = input("Would you like to play again? (y/n) ").lower()
        if play_again != 'y':
            print("Thanks for playing! Here's a summary of your game:")
            print(f"Number of guesses: {len(attempts)}")
            print(f"Mean of guesses: {statistics.mean(attempts)}")
            print(f"Median of guesses: {statistics.median(attempts)}")
            print(f"Mode of guesses: {statistics.mode(attempts)}")
            print(f"Number of highscore: {len(high_score)}")
            print(f"Mean of highscore: {statistics.mean(high_score)}")
            print(f"Median of highscore: {statistics.median(high_score)}")
            print(f"Mode of highscore: {statistics.mode(high_score)}")
            break  # Exit the game when the player chooses not to play again
        
start_game()
