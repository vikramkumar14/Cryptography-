import hashlib
import itertools

def find_collision():
    hash_table = {}
    while True:
        message = ''.join(chr(i) for i in range(256))  # Generate a message with all possible characters
        md5_hash = hashlib.md5(message.encode()).hexdigest()
        if md5_hash in hash_table:
            return message, hash_table[md5_hash]
        hash_table[md5_hash] = message

# Find a collision
message1, message2 = find_collision()

# Calculate the MD5 hash of both messages
md5_hash1 = hashlib.md5(message1.encode()).hexdigest()
md5_hash2 = hashlib.md5(message2.encode()).hexdigest()

print("Message 1:", message1)
print("MD5 Hash 1:", md5_hash1)
print()
print("Message 2:", message2)
print("MD5 Hash 2:", md5_hash2)
