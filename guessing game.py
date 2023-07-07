import random

print('Guessing game')

counter = 1
numberToGuess = random.randint(0, 10)

# Loop for the first two guesses
while counter <= 2:
    guess = int(input(f"{counter} out of 3 guesses, pick a number between 0 and 9: "))
    
    if guess == numberToGuess:
        print(f"Congratulations! You guessed correctly with {guess}.")
        break
    elif guess < numberToGuess:
        print(f"Sorry, your guess of {guess} is incorrect. Try a higher number!")
        counter += 1
    else:
        print(f"Sorry, your guess of {guess} is incorrect. Try a lower number!")
        counter += 1
    
    

# Last chance guess
while counter != 4:
    lastguess = int(input(f"{counter} out of 3 guesses, last chance, try again: "))
    if lastguess == numberToGuess:
        print(f"Congratulations! You guessed correctly with {lastguess}.")
        print(numberToGuess)
        break
    else:
        print(f"Sorry, game over. The correct number was {numberToGuess}.")
        print(numberToGuess)
        counter += 1