import hashlib

def calculate_md5_hash(message):
    md5_hash = hashlib.md5()
    md5_hash.update(message.encode())
    return md5_hash.hexdigest()

# Allow the user to input a plaintext message
message = input("Enter a message: ")

# Calculate the MD5 hash of the message
md5_hash = calculate_md5_hash(message)
print("MD5 Hash:", md5_hash)
