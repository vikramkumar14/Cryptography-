from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

def generate_rsa_keypair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def generate_aes_key():
    return get_random_bytes(16)

def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message)
    return ciphertext, tag, cipher.nonce

def decrypt_message(ciphertext, tag, nonce, key):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext

def sign_message(message, private_key):
    key = RSA.import_key(private_key)
    h = SHA256.new(message)
    signer = PKCS1_v1_5.new(key)
    signature = signer.sign(h)
    return signature

def verify_signature(message, signature, public_key):
    key = RSA.import_key(public_key)
    h = SHA256.new(message)
    verifier = PKCS1_v1_5.new(key)
    return verifier.verify(h, signature)

# Simulated communication between two parties
alice_private_key, alice_public_key = generate_rsa_keypair()
bob_private_key, bob_public_key = generate_rsa_keypair()

# Alice sends her public key to Bob
# Bob sends his public key to Alice

# Alice generates a shared secret key using Bob's public key
shared_secret_key = PBKDF2(bob_public_key, alice_private_key, 16)

# Alice encrypts a message for Bob
message_to_bob = b"Hello, Bob! This is Alice."
encrypted_message, tag, nonce = encrypt_message(message_to_bob, shared_secret_key)

# Alice signs the message
signature = sign_message(encrypted_message, alice_private_key)

# Bob decrypts the message
decrypted_message = decrypt_message(encrypted_message, tag, nonce, shared_secret_key)

# Bob verifies the signature
signature_valid = verify_signature(encrypted_message, signature, alice_public_key)

print("Decrypted Message (Bob):", decrypted_message.decode())
print("Signature Validity (Bob):", signature_valid)
