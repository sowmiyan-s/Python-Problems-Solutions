account = int(input("Enter Bank Balance : "))
price = int(input("Enter Product's Price : "))
if price > account:
    print("Insufficient Balance")
else:
    account = account - price
    account = account + ((price/10)*20)
    print("TOTAL BALANCE :", int(account)) 