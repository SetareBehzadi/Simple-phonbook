import json
import re


FILE_NAME = 'contact.json'


def load_contacts():
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}



def save_contacts(contacts):
    with open(FILE_NAME, 'w') as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("name: ").strip()
    mobile = input("mobile: ").strip()
    email = input("email: ").strip()

    mobile_pattern = re.compile(r'^\d{11}$')
    if not mobile_pattern.match(mobile):
        print("mobile is invalid ... must be 11 digits")
        return

    email_pattern = re.compile(r'^[^@]+@[^@]+\.[^@]+$')
    if not email_pattern.match(email):
        print("email is not valid, try again")
        return

    contacts[name] = {'mobile': mobile, 'email': email}
    print("add user successfully")
    save_contacts(contacts)


def edit_contact(contacts):
    name = input("Enter Name to Edit: ").strip()
    if name not in contacts:
        print("User Not Found")
        return

    mobile = input("new mobile number(Empty if you not to change): ").strip()
    email = input("new email(Empty if you not to change): ").strip()

    if mobile:
        mobile_pattern = re.compile(r'^\d{11}$')
        if not mobile_pattern.match(mobile):
            print("mobile is invalid ... must be 11 digits")
            return
        contacts[name]['mobile'] = mobile

    if email:
        email_pattern = re.compile(r'^[^@]+@[^@]+\.[^@]+$')
        if not email_pattern.match(email):
            print("email is not valid, try again")
            return
        contacts[name]['email'] = email

    print("user is updated successfully")
    save_contacts(contacts)


def delete_contact(contacts):
    name = input("Enter Name to Remove: ").strip()
    if name in contacts:
        del contacts[name]
        print("user is Deleted successfully")
        save_contacts(contacts)
    else:
        print("User Not Found")


def display_contacts(contacts):
    if not contacts:
        print("The List is Empty")
        return

    for name, info in contacts.items():
        print(f"name: {name}")
        print(f"mobile: {info['mobile']}")
        print(f"email: {info['email']}")
        print("-----")


def sort_contacts(contacts):
    sorted_contacts = dict(sorted(contacts.items()))
    print("Ordering User Successfully")
    return sorted_contacts
