"""
Password Manager

This is a simple password manager application implemented in Python. 
It allows users to securely store, retrieve, and delete passwords for various services. 
The passwords are encrypted using the `cryptography` library to ensure security.

Features:
- Encrypt and store passwords securely.
- Retrieve decrypted passwords when needed.
- Delete stored passwords.
- Uses a JSON file (`passwords.json`) to store encrypted passwords.
- Uses a key file (`key.key`) to store the encryption key.


"""

from cryptography.fernet import Fernet
import json
import os

class PasswordManager:
    def __init__(self, key_file='key.key', data_file='passwords.json'):
        self.key_file = key_file
        self.data_file = data_file
        self.key = self.load_key()
        self.fernet = Fernet(self.key)
        self.passwords = self.load_passwords()

    def load_key(self):
        # Load the encryption key from a file or generate a new one
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as file:
                return file.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as file:
                file.write(key)
            return key

    def load_passwords(self):
        # Load passwords from a JSON file
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                return json.load(file)
        else:
            return {}

    def save_passwords(self):
        # Save passwords to a JSON file
        with open(self.data_file, 'w') as file:
            json.dump(self.passwords, file, indent=4)

    def add_password(self, service, username, password):
        # Encrypt and add a new password
        encrypted_password = self.fernet.encrypt(password.encode()).decode()
        self.passwords[service] = {'username': username, 'password': encrypted_password}
        self.save_passwords()

    def get_password(self, service):
        # Decrypt and retrieve a password
        if service in self.passwords:
            encrypted_password = self.passwords[service]['password']
            decrypted_password = self.fernet.decrypt(encrypted_password.encode()).decode()
            return self.passwords[service]['username'], decrypted_password
        else:
            return None, None

    def delete_password(self, service):
        # Delete a password
        if service in self.passwords:
            del self.passwords[service]
            self.save_passwords()
            return True
        else:
            return False

# Test cases
if __name__ == "__main__":
    pm = PasswordManager()

    # Adding passwords
    pm.add_password('example.com', 'user1', 'password123')
    pm.add_password('another.com', 'user2', 'mypassword')

    # Retrieving passwords
    print("Password for example.com:")
    print(pm.get_password('example.com'))
    # Output: ('user1', 'password123')

    print("Password for another.com:")
    print(pm.get_password('another.com'))
    # Output: ('user2', 'mypassword')

    # Deleting a password
    pm.delete_password('example.com')
    print("Password for example.com after deletion:")
    print(pm.get_password('example.com'))
    # Output: (None, None)

    # Additional Test Cases

    # Test adding another password
    pm.add_password('newservice.com', 'user3', 'newpassword')
    print("Password for newservice.com:")
    print(pm.get_password('newservice.com'))
    # Output: ('user3', 'newpassword')

    # Test deleting a non-existent password
    result = pm.delete_password('nonexistent.com')
    print("Deleting nonexistent.com:")
    print(result)
    # Output: False

    # Test retrieving a non-existent password
    print("Password for nonexistent.com:")
    print(pm.get_password('nonexistent.com'))
    # Output: (None, None)
