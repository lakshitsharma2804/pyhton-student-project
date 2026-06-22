contact = {
    "lakshit":"9876543210",
    "rahul":"9876500000"
}
while True:
    choice = input("FEATURES\n" \
    "1.add contact\n" \
    "2.search contact\n" \
    "3.update contact\n" \
    "4.delete contact\n" \
    "5.view contact\n" \
    "6.exit\n"
    "what you want to do ? = ")

    if choice == "1":
        add_contact = input("enter contact name = ")
        add_number = input("enter number = ")
        if add_contact in contact:
            print("contact already added")
        else:
            contact[add_contact] = add_number
            print("contact added successfully")
    
    elif choice == "2":
        search_contact = input("search name = ").lower()
        if search_contact not in contact:
            print("not found")
        else:
            print("number = ", contact[search_contact])
    
    elif choice == "3":
        update_contact = input("enter name of contact which you want to be update = ")
        update_number = input("enter updated number = ")
        if update_contact not in contact:
            print("not found")
        else:
            contact[update_contact] = update_number
            print("contact updated succesfully")
    
    elif choice == "4":
        dlt_contact = input("enter name of contact which you want to delete = ")
        if dlt_contact not in contact:
            print("not found")
        else:
            del contact[dlt_contact]
            print("contact deleted succesfully")

    elif choice == "5":
        if len(contact) == 0:
            print("dictionary is empty")
        else:
            for key, value in contact.items():
                print(key, ":", value)
    
    elif choice == "6":
        print("ok bye!")
        break

    else:
        print("invalid command")