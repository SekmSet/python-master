# Écrire un programme qui convertit en m/h une vitesse donnée en km/h. Rappel : 1 mile = 1,609 km
# Bonus : Arrondir le résultat au centième près.

mile_in_km = 1.609
correct= False

print("I will convert your speed km/h to m/h")
response = input("Please enter a speed in km/h (ex. 50) : ")

while correct is not True:
    if response == "":
        print("To exit program enter exit value")
        response = input("Please enter a speed in km/h (ex. 50) : ")
        continue

    if response == "exit":
        correct = True
        continue

    convert_to_int = int(response)

    if convert_to_int == 0:
        print(f"Your result is - 0 m/h")
        correct = True
    else:
        convert = (convert_to_int/mile_in_km)

        round_convert_s1 = round(convert, 2)
        round_convert_s2 = format(convert,".2f")

        print(f"Your result with using the round() function is - {round_convert_s1} m/h")
        print(f"Your result with using the format() function is - {round_convert_s2} m/h")
        correct = True