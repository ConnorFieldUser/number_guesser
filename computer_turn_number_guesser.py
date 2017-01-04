
import random


def computer_number_guesser():
    player_number = int(input("Pick a number between 1 and 50 for the computer to guess: "))
    tries_left = 5
    low = 0
    high = 50
    if player_number > 0 and player_number < 50:
        for guess in range(5):
            computer_guess = random.randint(low, high)
            tries_left -= 1
            print(computer_guess)
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
        print("Between 1 and 50! Game over cheater.")

computer_number_guesser()
