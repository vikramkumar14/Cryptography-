def encrypt_rail_fence(message, num_rails):
    # Create rail fence pattern
    fence = [['\n' for _ in range(len(message))] for _ in range(num_rails)]
    rail = 0
    direction = -1
    
    for char in message:
        fence[rail][column] = char
        if rail == 0 or rail == num_rails - 1:
            direction = -direction
        rail += direction
    
    # Read off encrypted message
    encrypted_message = ''
    for rail in range(num_rails):
        for column in range(len(message)):
            if fence[rail][column] != '\n':
                encrypted_message += fence[rail][column]
    
    return encrypted_message

def decrypt_rail_fence(ciphertext, num_rails):
    # Create rail fence pattern
    fence = [['\n' for _ in range(len(ciphertext))] for _ in range(num_rails)]
    rail = 0
    direction = -1
    
    # Fill the fence with '*' to mark the positions of encrypted characters
    for i in range(len(ciphertext)):
        fence[rail][i] = '*'
        if rail == 0 or rail == num_rails - 1:
            direction = -direction
        rail += direction
    
    # Fill the fence with the characters of the ciphertext
    k = 0
    for rail in range(num_rails):
        for column in range(len(ciphertext)):
            if fence[rail][column] == '*' and k < len(ciphertext):
                fence[rail][column] = ciphertext[k]
                k += 1
    
    # Read off decrypted message
    decrypted_message = ''
    rail = 0
    direction = -1
    for i in range(len(ciphertext)):
        decrypted_message += fence[rail][i]
        if rail == 0 or rail == num_rails - 1:
            direction = -direction
        rail += direction
    
    return decrypted_message.replace('*', '')

# Test the program with different numbers of rails
plaintext = "Hello World!"
num_rails = 3  # Example number of rails

# Encrypt the message
encrypted_text = encrypt_rail_fence(plaintext, num_rails)
print("Encrypted message:", encrypted_text)

# Decrypt the ciphertext
decrypted_text = decrypt_rail_fence(encrypted_text, num_rails)
print("Decrypted message:", decrypted_text)
