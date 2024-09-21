import pickle
import os

# File to store contacts
CONTACTS_FILE = 'contacts.pkl'

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'rb') as f:
            return pickle.load(f)
    return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'wb') as f:
        pickle.dump(contacts, f)

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {
        'phone_number': phone_number,
        'email': email,
        'address': address
    }
    save_contacts(contacts)
    print("Contact added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}")
        print(f"Phone Number: {details['phone_number']}")
        print(f"Email: {details['email']}")
        print(f"Address: {details['address']}")
        print("-" * 40)

def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details['phone_number']:
            print(f"\nName: {name}")
            print(f"Phone Number: {details['phone_number']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['addres']}
