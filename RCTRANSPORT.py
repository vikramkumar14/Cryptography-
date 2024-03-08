import math

def encrypt(message, key):
    num_columns = len(key)
    num_rows = math.ceil(len(message) / num_columns)
    # Fill the grid with spaces
    grid = [[' ' for _ in range(num_columns)] for _ in range(num_rows)]
    
    # Fill the grid with the message
    for i, char in enumerate(message):
        row = i // num_columns
        col = i % num_columns
        grid[row][col] = char
    
    # Rearrange columns according to the key
    rearranged_columns = [col for _, col in sorted(zip(key, range(num_columns)))]
    
    # Read off the encrypted message
    encrypted_message = ''
    for col in rearranged_columns:
        for row in range(num_rows):
            encrypted_message += grid[row][col]
    
    return encrypted_message

def decrypt(ciphertext, key):
    num_columns = len(key)
    num_rows = math.ceil(len(ciphertext) / num_columns)
    # Fill the grid with spaces
    grid = [[' ' for _ in range(num_columns)] for _ in range(num_rows)]
    
    # Rearrange columns according to the key
    rearranged_columns = [col for _, col in sorted(zip(key, range(num_columns)))]
    
    # Calculate the number of characters in the last row
    chars_in_last_row = len(ciphertext) % num_columns
    
    # Fill the grid with the ciphertext
    k = 0
    for col in rearranged_columns:
        for row in range(num_rows):
            if row == num_rows - 1 and col >= chars_in_last_row:
                break
            grid[row][col] = ciphertext[k]
            k += 1
    
    # Read off the decrypted message
    decrypted_message = ''
    for row in range(num_rows):
        for col in range(num_columns):
            decrypted_message += grid[row][col]
    
    return decrypted_message

# Test the program with various plaintexts and keys
plaintext = "Hello World!"
key = [3, 1, 4, 2]  # Example key

# Encrypt the message
encrypted_text = encrypt(plaintext, key)
print("Encrypted message:", encrypted_text)

# Decrypt the ciphertext
decrypted_text = decrypt(encrypted_text, key)
print("Decrypted message:", decrypted_text)
