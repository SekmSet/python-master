class BankAccount:
    clients = []

    def __init__(self, name: str, balance: int):
        self.name = name
        self.balance = balance

        BankAccount.clients.append({"name": self.name, "balance": self.balance})

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"Your new balance account : {self.balance}")
        else:
            print("No money to deposit in yout account")

    def withdraw(self, money: int):
        if self.balance != 0 and self.balance - money >= 0:
            self.balance -= money
            print(f"Your new balance account : {self.balance}")
        else :
            print("You have not enough money")

    def display(self):
        print(f"ø Your name account : {self.name}")
        print(f"ø Your balance account : {self.balance}")

    def __str__(self):
        return f"Name - {self.name} and Balance - {self.balance}"

    def transfer(self, account, money: int):
        pass
        if self.balance != 0 and self.balance - money >= 0:
            for client in BankAccount.clients:
                if client.name == account.name:
                    client.balance += money
                    self.balance -= money
                else:
                    print("Client not found")
        else:
            print("You have not enough money")


print("----- CLIENT MOKA ------")
client_1 = BankAccount("Moka", 1000)
client_1.display() # Name = Moka and Balance = 1000
client_1.withdraw(500) # Name = Moka and Balance = 500
client_1.deposit(100) # Name = Moka and Balance = 600
client_1.display() # Name = Moka and Balance = 600

print("----- CLIENT OBRIGADA ------")
client_2 = BankAccount("Obrigada", 1000)

print(client_2) # Name = Obrigada and Balance = 1000
client_2.withdraw(1000) # Name = Obrigada and Balance = 0
client_2.deposit(100) # Name = Obrigada and Balance = 100
client_2.withdraw(200) # ERROR
print(client_2) # Name = Obrigada and Balance = 100

print("----- CLIENT MOKA DONNE DE L ARGENT A OBRIGADA ------")
client_1.transfer(client_2, 100) # Balance de Moka = 500 et Balance de Obrigada = 200

print(f"Client 1 : {client_1}")
print(f"Client 2 : {client_2}")