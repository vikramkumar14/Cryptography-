import hashlib

def calculate_hash(message):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(message.encode())
    return sha256_hash.hexdigest()

# Test the program with various messages
messages = [
    "Hello, World!",
    "This is a test message.",
    "Python is awesome!",
    "Hash functions are important for security.",
    "The quick brown fox jumps over the lazy dog."
]

# Calculate hash values for each message
for message in messages:
    hash_value = calculate_hash(message)
    print(f"Message: {message}")
    print(f"SHA-256 Hash: {hash_value}")
    print()
