#Guessing game- Diana, Azhar, Amonij, Felix
import random

def generate_random_number():
    return random.randint(1, 100)
print(generate_random_number())

def get_user_guess():
    while True:
        try:
            guess = int(input("Input guess: "))
            if guess >= 1 and guess <= 100:
                return guess
            else: 
                print("Enter a valid number.")
        except ValueError:
            print("Enter an integer.")

get_user_guess()

def game_loop():
    secret_number = generate_random_number()

    while True:
        guess = get_user_guess()

        if guess < secret_number:
            print("Try going higher")
        elif guess > secret_number:
            print("Try going lower")
        else:
            print(f"You did it, you guessed the correct number.")
            

if __name__ == "__main__": 
    game_loop()