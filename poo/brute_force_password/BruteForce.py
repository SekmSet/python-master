from random import randrange

# todo à faire


class BruteForce:

    def __init__(self, length):
        self.length = length

    def generate_password(self) -> str:
        password = ""

        for i in range(1, self.length + 1):
            random = randrange(65, 90)
            password += chr(random)
            i += 1
        return password

    def brut_force_password(self, password: str) -> list[str]:
        ascii_code = 65
        decrypt= []

        while decrypt != password:
            ascii = ascii_code
            string = ""
            for i in range(1, self.length+1):
                if i == 1:
                    letter = chr(ascii_code)
                    string += letter
                elif i == 2 :
                    letter = chr(ascii)
                    string += letter
                    ascii += 1

            decrypt.append(string)
            ascii_code += 1
        return decrypt


brutForce = BruteForce(2)
password = brutForce.generate_password()
print(password)
password_forced = brutForce.brut_force_password(password)
# print(password_forced)

# aa ab ac ad ae ...