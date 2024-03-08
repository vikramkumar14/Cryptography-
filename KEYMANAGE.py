from cryptography.fernet import Fernet

# Generate a new encryption key
def generate_key():
    return Fernet.generate_key()

# Store the encryption key securely
def store_key(key):
    with open("encryption_key.txt", "wb") as f:
        f.write(key)

# Retrieve the encryption key
def load_key():
    with open("encryption_key.txt", "rb") as f:
        return f.read()

# Test the key generation, storage, and retrieval
key = generate_key()
store_key(key)
loaded_key = load_key()

print("Generated Key:", key)
print("Loaded Key:", loaded_key)
print("Keys Match:", key == loaded_key)
