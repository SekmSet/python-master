# A l'aide de vos recherches, écrire une fonction permettant de générer une couleur [RGB] aléatoire.

# BONUS
# Écrire une seconde fonction s'appuyant sur la première,
# celle-ci permettra d'écrire un message d'une couleur aléatoire dans la console.

import random
from sty import fg

def generate_color():
    color = []
    count = 0

    while count != 3:
        random_number = random.randrange(0, 255)
        color.append(random_number)
        count += 1

    return color[0], color[1], color[2]

def display_with_color(color, text):
    print(fg(color[0], color[1], color[2]), text)

text = input("Your text : ")

color = generate_color()
display_with_color(color, text)