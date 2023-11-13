# Le programme tire un nombre aléatoire entre 0 et 100. Ensuite, la personne doit trouver le nombre en recevant comme indication si le nombre est trop grand ou trop petit.
# A la fin, le programme doit dire combien de coups ont été joués.
#
# BONUS
# Faire un menu permettant de choisir une difficulté : Facile : 0 à 10.
# Moyen : 0 à 100.
# Difficile : 0 à 1000.

import random

def select_game_level() :
    print("Game difficulty ")
    print("Easy : 0 - 10")
    print("Normal : 0 - 100")
    print("Hard : 0 - 1000")

    start = 0
    stop = 0

    while stop == 0:
        game_difficulty = input("Select a game difficulty : ")

        if game_difficulty == "Easy":
            stop = 10
        elif game_difficulty == "Normal":
            stop = 100
        elif game_difficulty == "Hard":
            stop = 1000
        else:
            print("I didn't understand")

    return [start, stop]


def retry_game(retry):
    response_retry = input("Do you want play again ? (Y/N) ")

    if response_retry == "N":
        retry = False

    return retry


def play_round(counter, number_of_party, random_number, retry, win):
    while win is not True:
        response_proposition = input("Your proposition : ")

        if response_proposition == "":
            print("You have to give me a number 0_0")
            continue

        response_to_int = int(response_proposition)
        counter += 1

        if response_to_int == random_number:
            number_of_party += 1

            print("IT S A WINN *_*")
            print(f"Number of try {counter}")
            print(f"Number of party {number_of_party}")

            retry = retry_game(retry, number_of_party)
            win = True
        elif response_to_int > random_number:
            print("Nooooo, it's LESS")
        elif response_to_int < random_number:
            print("Nooooo, it's MORE")
    return [retry, number_of_party]


def play_game():
    retry = True
    number_of_party = 0

    print("Let's play a game with to find the secret number")

    while retry is not False:
        [start, stop] = select_game_level()

        random_number = random.randrange(start, stop)

        print("Your time to play, you have to find my secret number !")

        win = False
        counter = 0

        [retry, number_of_party] = play_round(counter, number_of_party, random_number, retry, win)


play_game()