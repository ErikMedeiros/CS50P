# https://cs50.harvard.edu/python/2022/psets/2/coke/

amount_due, change_owed, valid_coins = 50, 0, [25, 10, 5]

while amount_due > 0:
    print("Amount Due: ", amount_due)
    coin = int(input("Insert Coin: "))

    if coin in valid_coins:
        amount_due -= coin
        change_owed = amount_due * -1

print("Change Owed:", change_owed)
