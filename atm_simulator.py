initial_balance = 10000
print("Welcome To ATM Simulator")
print(initial_balance)
while True:
     choice = input(
        "\nATM Machine\n"
        "1. Check Balance\n"
        "2. Deposit Money\n"
        "3. Withdraw Money\n"
        "4. Exit\n"
        "Enter Choice = "
    )
   
     if choice == "1":
        print("Current Balance = ", initial_balance)

     elif choice == "2":
        deposit_money = int(input("Enter Amount = "))
        if (deposit_money) <= 0:
            print("Invalid Depoist")
        else:
            initial_balance += deposit_money
            print("Current Balance = ", initial_balance)
            print("Amount Added Successfully")

    

     elif choice == "3":
        withdraw_money = int(input("Enter Amount = "))
        if withdraw_money <= 0:
            print("Invalid Amount")
        elif  initial_balance < (withdraw_money):
            print("Insufficient Balance")
        else:
            initial_balance -= withdraw_money
            print("Current Balance = ", initial_balance)
            print("Amount Withdraw Successfully")


     elif choice == "4":
        print("Thank You")
        print("Bank Closed")
        break

     else:
        print("invalid command")

    
