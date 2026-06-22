passwords = {
    "instagram": "abc123",
    "facebook": "xyz456",
    "gmail": "pass789"
}
while True:

    choice = input(
        "\nPassword Manager\n" \
        "1. View Passwords\n" \
        "2. Search Account\n" \
        "3. Add Account\n" \
        "4. Exit\n" \
        "Enter Choice = "
    )

    if choice == "1":
        for key, value in passwords.items():
            print(key, ":", value)

    elif choice == "2":
        search_account = input("Enter Account Name = ")
        if search_account in passwords:
            print("password = ", passwords[search_account] )
        else:
            print("Account Not Found")

    elif choice == "3":
        new_account = input("Enter Account Name = ")
        account_pass = input("Enter Password = ")
        if new_account in passwords:
            print("Account Already Exists")
        else:
            passwords.update({new_account : account_pass})
            print("Account Added Succesfully")
    
    elif choice == "4":
        print("Thank You")
        print("Program Closed")
        break

    else:
        print("Invalid Command")