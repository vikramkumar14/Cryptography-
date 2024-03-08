def mod_exp(base, exp, modulus):
    result = 1
    base = base % modulus
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % modulus
        exp = exp >> 1
        base = (base * base) % modulus
    return result

def diffie_hellman(prime, primitive_root):
    private_key = int(input("Enter your private key: "))
    public_key = mod_exp(primitive_root, private_key, prime)
    return public_key

def secret_key_exchange(prime, primitive_root):
    alice_public = diffie_hellman(prime, primitive_root)
    bob_public = diffie_hellman(prime, primitive_root)
    shared_secret_alice = mod_exp(bob_public, alice_private, prime)
    shared_secret_bob = mod_exp(alice_public, bob_private, prime)
    print("Shared Secret Key (Alice):", shared_secret_alice)
    print("Shared Secret Key (Bob):", shared_secret_bob)

# Test the program with different prime numbers and primitive roots
prime = 23
primitive_root = 5
alice_private = 6
bob_private = 15

secret_key_exchange(prime, primitive_root)
