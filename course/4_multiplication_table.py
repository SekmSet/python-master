# L’utilisateur entre un nombre.
# Le programme stock les 10 premiers résultats de la table de multiplication choisie par l’utilisateur dans une liste
# puis affiche cette liste.

# BONUS
# Signaler au passage, à l’aide d’une astérisque, ceux qui sont des multiples de 3

index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []
result_with_multiples_of_3 = []

multiplication_table = input("Witch table do you want calculate ? ")

while multiplication_table == "":
    print("I didn't understand.")

multiplication_table_to_int = int(multiplication_table)

for i in index:
    calcul = i * multiplication_table_to_int
    result.append(calcul)

    if calcul % 3 == 0:
        str = f"{calcul}*"
        result_with_multiples_of_3.append(str)
    else:
        result_with_multiples_of_3.append(calcul)

print(result)
print(result_with_multiples_of_3)
