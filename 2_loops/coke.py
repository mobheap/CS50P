accepted = [25,10,5]
price = 50
while price > 0:
    print("Amount Due:", price)
    paid = int(input("Insert Coin: "))
    if paid in accepted:
        price -= paid
change = abs(price)
print("Change Owed:", change)