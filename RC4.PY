def rc4(key, message):
    S = list(range(256))
    j = 0
    out = []

    # KSA (Key Scheduling Algorithm)
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # PRGA (Pseudo-Random Generation Algorithm)
    i = j = 0
    for char in message:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))

    return ''.join(out)

# Test the program
key = [0x1a, 0x2b, 0x3c, 0x4d, 0x5e]  # Example key
message = "Hello, World!"

# Encrypt the message
encrypted_message = rc4(key, message)
print("Encrypted Message:", encrypted_message)

# Decrypt the message
decrypted_message = rc4(key, encrypted_message)
print("Decrypted Message:", decrypted_message)
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
