from BankAccount import BankAccount


class SavingAccount(BankAccount):
    annual_interest = 5

    def __init__(self, name: str, balance: int):
        BankAccount.__init__(self, name, balance)

    def saving(self, placement: float) -> float:
        daily_capitalization = placement * (1 + SavingAccount.annual_interest / 12 / 100) ** (2 * 12)
        daily_capitalization = float(format(daily_capitalization, ".2f"))

        self.balance = daily_capitalization
        return float(format(daily_capitalization - placement, ".2f"))


print("----- SAVINGS ------")
client = SavingAccount("Le chat", 5000)
annual_savings = client.saving(1000)
print(annual_savings)
