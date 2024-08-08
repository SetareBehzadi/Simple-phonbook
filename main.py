from operation import *
import sys


def main():
    contacts = load_contacts()
    try:
        print('''
        Welcome to the Phone Directory
        ------------------------------
        1) Add New Contact
        2) Update Contact
        3) Delete Contact
        4) Show All Contacts
        5) Sort Contact
        0) Quit
    ''')

        choice = input("Select any one of the option above:\t").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            edit_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            display_contacts(contacts)
        elif choice == '5':
            contacts = sort_contacts(contacts)
            save_contacts(contacts)
        elif choice == '6':
            print("Exit...")
            sys.exit()
        else:
            print("Try again... You choose wrong number!")

    except Exception as e:
        print(f"Unknown exception occured: {e}")



if __name__ == "__main__":
    main()