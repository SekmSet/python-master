# Créer un nouveau fichier customers.py.
# A l'aide de listes et de dictionnaires,
# trouver le meilleur moyen de stocker toutes les données ci-contre dans une seule et unique variable.

client_1 = {
    "Nom" : "Doe",
    "Prenom" : "John",
    "Age" : 21,
    "Email" : "john.doe@xyz.com",
    "Hobbies" : "Karaté, Tennis",
}

client_2 = {
    "Nom" : "Stewart",
    "Prenom" : "Jane",
    "Age" : 26,
    "Email" : "" ,
    "Hobbies" : "Danse, Peinture, Chant",
}

client_3 = {
    "Nom" : "Tardieu",
    "Prenom" : "Olivier",
    "Age" : 32,
    "Email" : "olivier.tardieu@xyz.com",
    "Hobbies" : "",
}

clients = [
    client_1,
    client_2,
    client_3
]

print(clients)