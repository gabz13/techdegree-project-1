import random

guesses_list = []


def display_score():
    if len(guesses_list) <= 0:
        print("The high score is all yours, as long as you play of course!")
    else:
        print("The current high score is {} attempts".format(min(guesses_list)))


def start_game():
    random_number = int(random.randint(1, 60))
    print("Hey there! Welcome to the number guessing game!")
    player_name = input("What's your name? ")
    lets_play = input("Hi, {}, would you like to play the number guessing game? (Yes/No) ".format(player_name))
    guesses = 0
    display_score()
    while lets_play.lower() == "yes":
        try:
            guess = input("Pick a number between 1 and 60 ")
            if int(guess) < 1 or int(guess) > 60:
                raise ValueError("Please guess a number within the given range")
            if int(guess) == random_number:
                print("Awesome! You got it!")
                guesses += 1
                guesses_list.append(guesses)
                print("It took you {} attempts".format(guesses))
                play_again = input("Would you like to play again? (Yes/No) ")
                guesses = 0
                display_score()
                random_number = int(random.randint(1, 60))
                if play_again.lower() == "no":
                    print("Thanks for playing!")
                    break
            elif int(guess) > random_number:
                print("Too high, guess lower")
                guesses += 1
            elif int(guess) < random_number:
                print("Too low, guess higher")
                guesses += 1
        except ValueError as err:
            print("Oh no!, that is not a valid value. Try again...")
            print("({})".format(err))
    else:
        print("Thanks for playing!")


if __name__ == '__main__':
    start_game()
