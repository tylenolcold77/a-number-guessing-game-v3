import random
import statistics

def start_game():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    
    high_score = float("inf")
    
    while True:
        winning_number = random.randint(1, 100)
        print(f"Can you beat the current high score of {high_score} attempts?")
        
        attempts = []

        while True:
            try:
                guess = int(input("Take a guess:"))
                if guess < 1 or guess > 100:
                    print("Your guess is outside the range 0f 1-100. Try again.")
                    continue
            except ValueError:
                print("Please enter a valid whole number.")
                continue
            
            attempts.append(guess)
            
            if guess < winning_number:      
                print("Too low! Try a higher number.")
            elif guess > winning_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed the number in {len(attempts)} attempts!")
                if len(attempts) < high_score:
                    high_score = len(attempts)
                    print(f"New high score! {len(attempts)} attempts.")
                break
            
        play_again = input("Would you like to play again? (y/n) ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Here's a summary of your game:")
            print(f"Number of guesses: {len(attempts)}")
            print(f"Mean of guesses: {statistics.mean(attempts)}")
            print(f"Median of guesses: {statistics.median(attempts)}")
            print(f"Mode of guesses: {statistics.mode(attempts)}")
            break
        
start_game()

