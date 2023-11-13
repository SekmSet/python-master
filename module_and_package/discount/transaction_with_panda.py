from pandas import read_excel, DataFrame

reduction = 10
file_name = "transactions.xlsx"

e_file = read_excel(
    file_name,
    engine='openpyxl'
)

print(e_file)

prices = e_file['price']
new_prices = []

for price in prices:
    new_price = float(price) * (1 - (reduction/100))
    new_prices.append(format(new_price,".2f"))

e_file['corrected'] = new_prices

e_file.to_excel("New_transaction_panda.xlsx", "Sheet_name")
