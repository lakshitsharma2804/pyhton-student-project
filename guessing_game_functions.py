import random

def setup():
    return random.randint(1, 10)

def get_guess():
    return int(input("Enter Number: "))

def check_guess(guess, secret):
    if guess < secret:
        return "Low"
    elif guess > secret:
        return "High"
    else:
        return "Correct"

def play():
    secret = setup()

    while True:
        guess = get_guess()
        result = check_guess(guess, secret)

        print(result)

        if result == "Correct":
            break

play()