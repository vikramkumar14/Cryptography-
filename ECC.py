import hashlib
import ecdsa

# Generate ECC key pair
def generate_ecc_keypair():
    private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    public_key = private_key.get_verifying_key()
    return private_key, public_key

# Encrypt a message using ECC
def ecc_encrypt(public_key, message):
    hash_message = hashlib.sha256(message.encode()).digest()
    signature = private_key.sign(hash_message)
    return signature

# Decrypt a message using ECC
def ecc_decrypt(signature, public_key):
    try:
        public_key.verify(signature, hash_message)
        return True
    except ecdsa.BadSignatureError:
        return False

# Test the program
private_key, public_key = generate_ecc_keypair()
print("Private Key:", private_key.to_string().hex())
print("Public Key:", public_key.to_string().hex())

message = "Hello, World!"
signature = ecc_encrypt(public_key, message)
print("Signature:", signature.hex())

verification_result = ecc_decrypt(signature, public_key)
if verification_result:
    print("Message verified: The signature is valid.")
else:
    print("Message verification failed: The signature is invalid.")
