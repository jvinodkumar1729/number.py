import random

def game():
    number = random.randint(0, 100)
    tries = 1
    done = False

    while not done:
        guess = int(input("Enter a guess: "))

        if guess == number:
            done = True
            print(f"This is correct! You won! You needed {tries} tries.")
        else:
            tries += 1
            if guess > number:
                print("The actual number is smaller. Please try again.")
            else:
                print("The actual number is larger. Try again, buddy.")

            if tries > 5:
                print("Sorry, this was too many tries. Start over.")
                break

# Call the game function to start playing
game()
