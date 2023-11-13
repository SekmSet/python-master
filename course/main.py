first_name = "John"
last_name = "Doe"

print("> Stewart : Welcome on board !")
username = input("> Stewart : Your last username : ")
print(f"> {first_name} {last_name} : {username} ")
print(f"> Stewart : Hello {username} !")

print("--------------")

def get_max(numbers:list[float]) -> float:
    number = numbers[0]
    for num in numbers:
        if number < num:
            number = num
    return number

result = get_max([1.2,11.4,5.9])
print(result)

print("--------------")