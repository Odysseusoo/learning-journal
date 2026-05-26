amount_due = 50
while amount_due > 0:
    coin = int(input(f"Amount Due: {amount_due}\nInsert Coin: "))
    if coin == 25:
        amount_due -= 25

    elif coin == 10:
        amount_due -= 10

    elif coin == 5:
        amount_due -= 5

print (f"Change Owed: {abs(amount_due)}")