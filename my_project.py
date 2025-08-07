

contact_book=[]
def add():
    while True:
        name=input("Enter your name:")
        if len(name)<=15:
         break
        else:
            print("length must be 15")
    while True:
        phone=input("Enter your phone  no:")
        if len(phone)==11 and phone.isdigit():
            break
        else:
            print("Phone no must be 11 digits and numeric")
    while True:
       email=input("Enter your email:")
       if '@' in email:
           break
       else:
           print("Invalid email must conatain @ symbol")
    d={"Name":name,"Phone No":phone,"Email":email}
    contact_book.append(d)
    print("Contact added successfully*********")
    print(contact_book)
def view_contacts():
    print(" contact list")
    print()
    print(f"{'Name':<15}{'Phone No':<15}{'Email'}")
    print()
    for i in contact_book:
       print(f"{i['Name']:<15}{i['Phone No']:<15}{i['Email']}")
def search():
    name=input("enter your name:")
    found=False

    for i in contact_book:
        if i['Name'].lower()==name.lower():
            print(f"{i['Name']:<15}{i['Phone No']:<15}{i['Email']}")
            found=True
            break
    if not found:
            print("Contact not found")
def delete_contact():
    name=input("enter name which you want to delete:")
    found=False
    for i in contact_book:
        if i['Name'].lower()==name.lower():
            contact_book.remove(i)
            print("contact deleted successfully")
            print(contact_book)
            found=True
            break
    if not found:
        print("contact not found")
def update():
        name = input("Enter name which you want to enter:")
        found = False
        for i in contact_book:
            if i['Name'].lower() == name.lower():
                found = True

                ch = input("What do you want to update Name/Phone/Email:")
                if ch.lower() == "name":
                    n = input("Enter new name :")
                    i['Name'] = n
                elif ch.lower() == "phone":
                    p = print("Enter new phone :")
                    i['Phone'] = p
                elif ch.lower() == "email":
                    e = print("Enter new email :")
                    i['Email'] = e
                else:
                    print("Invalid option.please enter name/phone/email")
        if not found:
            print("Contact not found")
while True:
    show='''
    please select any one option:
    1.Add contact
    2.view all contact list
    3.search conatct
    4.delete contact
    5.update contact
    6.Exit
    '''
    print(show)
    choice=int(input("Enter any one option:"))
    if choice==1:
        add()
    elif choice==2:
        view_contacts()
    elif choice==3:
        search()
    elif  choice==4:
        delete_contact()
    elif choice==5:
        update()
    elif choice==6:
        print("Exit")
        break
    else:
        print("Invalid option.Please try again!")





