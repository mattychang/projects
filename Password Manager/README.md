# Password Manager
## Author: Matthew Chang

This is a simple password manager application implemented in Python. It allows users to securely store, retrieve, and delete passwords for various services. The passwords are encrypted using the `cryptography` library to ensure security.

## Features

- Encrypt and store passwords securely.
- Retrieve decrypted passwords when needed.
- Delete stored passwords.
- Uses a JSON file (`passwords.json`) to store encrypted passwords.
- Uses a key file (`key.key`) to store the encryption key.

## Setup

1. **Install the required dependencies:**
```sh
pip install cryptography
```

## Usage

### Adding a Password
```python

pm = PasswordManager()
pm.add_password('example.com', 'user1', 'password123')

```
### Retrieving a Password
```python

username, password = pm.get_password('example.com')
print(f'Username: {username}, Password: {password}')

```

### Deleting a Password
```python

pm.delete_password('example.com')

```
