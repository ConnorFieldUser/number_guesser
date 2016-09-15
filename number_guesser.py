
import random


def number_guesser():
    cpu_num = random.randint(1, 25)
    tries_left = 5
    for guess in range(5):
        player_guess = input("You have {} guesses left. Try to guess my number: ".format(tries_left))
        tries_left -= 1
        if cpu_num == int(player_guess):
            print("You win! The number was {}".format(cpu_num))
            break
        elif cpu_num > int(player_guess):
            print("Thats not it. My number is greater than that.")
        elif cpu_num < int(player_guess):
            print("Nope. My number is smaller than that.")
        elif type(player_guess) != int:
            print("Numbers only")
    else:
        print("Game Over!")


number_guesser()
