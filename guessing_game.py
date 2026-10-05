import random

number = random.randint(1, 100)
attempts = 0

print("================================")
print("      NUMBER GUESSING GAME")
print("================================")
print("Guess a number between 1 and 100")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("\nCongratulations! 🎉")
            print("You guessed the number:", number)
            print("Number of attempts:", attempts)
            break

    except ValueError:
        print("Please enter a valid number.")
