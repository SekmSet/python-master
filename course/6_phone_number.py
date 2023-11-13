# Écrire un programme qui épellera un numéro de téléphone en toute lettre.

numbers = {
    0: "zero",
    1 : "one",
    2: "two",
    3: "tree",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    "+" : "Plus"

}

phone_number = input("Numéro de téléphone ")

phone_number_string = ""
for element in phone_number:
    if element != "+":
        element = int(element)

    phone_number_string += f"{numbers[element]} "

print(phone_number_string.strip())