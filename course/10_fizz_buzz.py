# Le Fizz Buzz est un exercice courant en entretien d'embauche.

# Pour chaque multiple de 3 : Afficher Fizz
# Pour chaque multiple de 5 : Afficher Buzz
# Pour les multiples de 3 et 5 : Afficher Fizz Buzz
# Pour tous les autres : Afficher le nombre

def fizz_buzz(num):
    if num % 5 == 0 and num % 3 == 0:
        print("Fizz Buzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


number = input("Give me a number : ")
number = int(number)
count = 1

while count <= number :
    fizz_buzz(count)
    count += 1