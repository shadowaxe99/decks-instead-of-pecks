```python
from cryptography.fernet import Fernet

# Generate a key for encryption and decryption
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the previously generated key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt the data
def encrypt_data(influencer_id, data):
    key = load_key()
    f = Fernet(key)
    encrypted_data = f.encrypt(data)
    return encrypted_data

# Decrypt the data
def decrypt_data(influencer_id, encrypted_data):
    key = load_key()
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    return decrypted_data
```