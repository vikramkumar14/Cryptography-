import hashlib
import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)
    d = mod_inv(e, phi)
    return ((e, n), (d, n))

def sign(private_key, message):
    d, n = private_key
    hashed_message = int.from_bytes(hashlib.sha256(message.encode()).digest(), byteorder='big')
    signature = pow(hashed_message, d, n)
    return signature

def verify(public_key, message, signature):
    e, n = public_key
    hashed_message = int.from_bytes(hashlib.sha256(message.encode()).digest(), byteorder='big')
    decrypted_signature = pow(signature, e, n)
    return hashed_message == decrypted_signature

# Generate prime numbers for RSA
p = 61
q = 53

# Generate RSA key pair
public_key, private_key = generate_keypair(p, q)
print("Public Key:", public_key)
print("Private Key:", private_key)

# Message to be signed
message = "Hello, World!"

# Generate digital signature
signature = sign(private_key, message)
print("Digital Signature:", signature)

# Verify the authenticity of the message using the digital signature
is_authentic = verify(public_key, message, signature)
if is_authentic:
    print("The message is authentic.")
else:
    print("The message is not authentic.")
