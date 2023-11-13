# Écrire dans un nouveau fichier
# Un programme qui permettra de jouer à Pierre / Feuille / Ciseaux contre l'ordinateur en 2 manches gagnantes.

import random

player = {
    "victory": 0,
    "choice": ""
}

computeur = {
    "victory": 0,
    "choice": ""
}

choices = ["pierre", "feuille", "ciseau"]
array_len = len(choices)
round = 0


while round <= 3:
    computeur["choice"] = choices[random.randrange(0, array_len)]
    player["choice"] = input("Your choice (pierre / feuille / ciseau) : ")

    round += 1

    if player["choice"] == computeur["choice"]:
        print("Match null")
        continue
    elif ((player["choice"] == "pierre" and computeur["choice"] == "ciseau")
          or (player["choice"] == "feuille" and computeur["choice"] == "pierre")
          or (player["choice"] == "ciseau" and computeur["choice"] == "feuille")):
        player["victory"] += 1
    else:
        computeur["victory"] += 1

print("--------------------------------")
if computeur["victory"] == player["victory"]:
    print("match null")
elif computeur["victory"] > player["victory"]:
    print("player defeat")
else:
    print("player win")

print(f"computeur victory {computeur['victory']}")
print(f"player victory {player['victory']}")