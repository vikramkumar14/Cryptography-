import hashlib

def generate_mac(secret_key, message):
    # Combine the secret key and message
    combined_message = secret_key.encode() + message.encode()
    # Compute the MD5 hash of the combined message
    md5_hash = hashlib.md5(combined_message).hexdigest()
    return md5_hash

def verify_mac(secret_key, message, original_mac):
    # Generate MAC using the provided secret key and message
    mac = generate_mac(secret_key, message)
    # Compare the generated MAC with the original MAC
    return mac == original_mac

# Test the program
secret_key = "secret_key"
message = "Hello, World!"

# Generate MAC
mac = generate_mac(secret_key, message)
print("Generated MAC:", mac)

# Verify MAC
is_valid = verify_mac(secret_key, message, mac)
if is_valid:
    print("MAC is valid. Message integrity verified.")
else:
    print("MAC is invalid. Message integrity compromised.")
