print("Amount Due: 50")
amount = 0

while amount < 50:
    in_coin = int(input("Insert Coin: "))
    if in_coin == 5 or in_coin == 10 or in_coin == 25:
        amount = amount + in_coin
    print("Amount Due:", 50 - amount)

print("Change Owed:", amount - 50)
