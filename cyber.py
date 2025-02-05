import os
from cryptography.fernet import Fernet

# Function to generate a key and save it to a file
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the encryption key from a file
def load_key():
    return open("key.key", "rb").read()

# Encrypt and save the password.;
def save_password(service, password):
    key = load_key()
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    
    with open("passwords.txt", "a") as file:
        file.write(f"{service}: {encrypted_password.decode()}\n")
    print(f"Password for {service} saved successfully!")

# Retrieve and decrypt a password
def retrieve_password(service):
    key = load_key()
    fernet = Fernet(key)
    
    try:
        with open("passwords.txt", "r") as file:
            for line in file:
                stored_service, encrypted_password = line.strip().split(": ")
                if stored_service == service:
                    decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()
                    return decrypted_password
        return "Service not found!"
    except FileNotFoundError:
        return "No passwords stored yet!"

# Main menu
if not os.path.exists("key.key"):
    generate_key()

while True:
    print("\nPassword Manager")
    print("1. Save a password")
    print("2. Retrieve a password")
    print("3. Exit")
    choice = input("Enter your choice: ")
        
    if choice == "1":
        service = input("Enter the service name: ")
        password = input("Enter the password: ")
        save_password(service, password)
    elif choice == "2":
        service = input("Enter the service name: ")
        print(f"Password for {service}: {retrieve_password(service)}")
    elif choice == "3":
        print("Exiting Password Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")