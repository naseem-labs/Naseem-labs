print ("====Naseem labs contact Book====")
contact = {}

while True:
    print("\n1. Add contact")
    print ("2.Search contact")
    print ("3. Show all contact")
    print("4. delete contact")
    print("5. quit")

    choice = input("\nChoose (1-5): ")
    
    if choice =="1":
        name = input("name: ")
        phone = input("phone: ")
        contact[name] = phone
        print(f"✅ {name} added!")
    elif choice == "2":
        name = input("Search name: ")
        if name in contact:
            print(f"📞 {name} = {contact[name]}")
        else:
            print("❌ not found")
    elif choice == "3":
        if contact:
            print(f"\n 📋 all contact")
            for name, phone in contact.items():
                print(f" {name} : {phone}")
        else:
            print("no contact yet")
    elif choice == "4":
        name = input("Delete name: ")
        if name in contact:
            del contact [name]
            print(f"{name} is deleted.")
        else:
            print ("not found!")
    elif choice == "5":
        print("thank you, bye!")
        break
    else:
        print ("invalid choice")
