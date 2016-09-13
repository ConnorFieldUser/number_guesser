
import random


def computer_number_guesser():
    player_number = int(input("Pick a number between 1 and 25 for the computer to guess: "))
    tries_left = 5
    low = 0
    high = 25
    if player_number > 0 and player_number < 25:
        for guess in range(5):
            computer_guess = random.randint(low, high)
            tries_left -= 1
            if computer_guess == player_number:
                print("Computer wins! Your number was {}".format(player_number))
                break
            elif computer_guess > player_number:
                print("Lower")
                high = computer_guess
            elif computer_guess < player_number:
                print("Higher")
                low = computer_guess
            else:
                print("{}: Fail".format(computer_guess))
        else:
            print("Game Over. You win!")
    else:
        print("Between 1 and 25! Game over cheater.")

# low=0, reset low, ect
computer_number_guesser()
