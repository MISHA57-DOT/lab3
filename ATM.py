balance = 50000
while True:
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    if(choice==1):
        print("Your balance is:",balance)
    elif(choice==2):
        print("how much u want to deposit")
        deposit=int(input("Enter your deposit: "))
        balance+=deposit
    elif(choice==3):
        print("enter how much u want to withdraw")
        withdraw=int(input("Enter your withdraw: "))
        if(withdraw>balance):
            print("insufficient amount")
        else:
            balance-=withdraw

    elif(choice==4):
        break
    else:
        print("enter correct choice")