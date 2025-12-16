import random

def number_guessing_game():
    secret_number = random.randint(1, 10)
    attempts = 0

    while True:
        guess = int(input("Guess the number (1 to 10): "))
        attempts += 1

        if guess > secret_number:
            print("Too high")
        elif guess < secret_number:
            print("Too low")
        else:
            print("🎉 Correct! You guessed the number")
            print("Total attempts:", attempts)
            break
while True:
    number_guessing_game()
    play_again =input("Do you want to play again?(yes/no) : ").lower()
    
    if play_again != "yes":
        print("Thanks for playing ")
        break