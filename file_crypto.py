from cryptography.fernet import Fernet
import os

# Function to generate a key and save it
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as secret.key")

# Function to load the key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt a file
def encrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(filename + ".enc", "wb") as file:
        file.write(encrypted_data)

    print(f"{filename} encrypted successfully!")

# Decrypt a file
def decrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    try:
        decrypted_data = f.decrypt(encrypted_data)
        new_filename = filename.replace(".enc", "")
        with open(new_filename, "wb") as file:
            file.write(decrypted_data)
        print(f"{filename} decrypted successfully!")
    except Exception as e:
        print("Error: Invalid key or corrupted file!")

if __name__ == "__main__":
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")

    choice = input("Choose an option: ")

    if choice == "1":
        generate_key()
    elif choice == "2":
        filename = input("Enter file name to encrypt: ")
        encrypt_file(filename)
    elif choice == "3":
        filename = input("Enter file name to decrypt: ")
        decrypt_file(filename)
    else:
        print("Invalid choice!")