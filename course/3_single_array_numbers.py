# Écrire un programme qui créera une nouvelle liste en ne gardant que les valeurs uniques.

numbers = [8, 7, 11, 7, 2, 10, 5, 8]
numbers_filtered = []

for number in numbers:
    if number not in numbers_filtered:
        numbers_filtered.append(number)

print(numbers_filtered)