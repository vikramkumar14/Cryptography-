import numpy as np

def hill_encrypt(plaintext, key):
    # Convert plaintext to uppercase and remove spaces
    plaintext = plaintext.upper().replace(" ", "")
    
    # Pad the plaintext if necessary
    if len(plaintext) % 2 != 0:
        plaintext += 'X'
    
    # Initialize the ciphertext
    ciphertext = ""
    
    # Perform encryption for each pair of characters in the plaintext
    for i in range(0, len(plaintext), 2):
        # Convert pair of characters to numeric values
        block = [ord(char) - ord('A') for char in plaintext[i:i+2]]
        
        # Matrix multiplication: key * block
        encrypted_block = np.dot(key, block) % 26
        
        # Convert encrypted block back to characters
        ciphertext += ''.join([chr(char + ord('A')) for char in encrypted_block])
    
    return ciphertext

def hill_decrypt(ciphertext, key):
    # Calculate the inverse of the key matrix modulo 26
    key_inv = np.linalg.inv(key)
    key_inv = np.round(key_inv * np.linalg.det(key) * np.linalg.inv(key).astype(int)) % 26
    
    # Initialize the plaintext
    plaintext = ""
    
    # Perform decryption for each pair of characters in the ciphertext
    for i in range(0, len(ciphertext), 2):
        # Convert pair of characters to numeric values
        block = [ord(char) - ord('A') for char in ciphertext[i:i+2]]
        
        # Matrix multiplication: key_inv * block
        decrypted_block = np.dot(key_inv, block) % 26
        
        # Convert decrypted block back to characters
        plaintext += ''.join([chr(int(char) + ord('A')) for char in decrypted_block])
    
    return plaintext

def main():
    # Example key matrix for 2x2 Hill cipher
    key = np.array([[6, 24], [1, 13]])
    
    # Example plaintext
    plaintext = "HELLO"
    
    # Encrypt the plaintext
    ciphertext = hill_encrypt(plaintext, key)
    print("Ciphertext:", ciphertext)
    
    # Decrypt the ciphertext
    decrypted_text = hill_decrypt(ciphertext, key)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
