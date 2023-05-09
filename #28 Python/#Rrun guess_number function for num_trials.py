#This code will run guess_number function for num_trials times, and output the results for each trial.
import random

def get_random_number():
    return random.randint(1, 100)

def guess_number():
    random_number = get_random_number()
    num_guesses = 0

    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        num_guesses += 1
        
        if guess == random_number:
            print(f"Congratulations! You guessed the number in {num_guesses} guesses.")
            break
        elif guess < random_number:
            print("Too low! Guess again.")
        else:
            print("Too high! Guess again.")

def show_results(num_trials):
    for i in range(num_trials):
        print(f"Trial #{i+1}:")
        guess_number()
show_results(3)