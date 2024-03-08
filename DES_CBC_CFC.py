def des_encrypt(message, key, mode, iv=None):
  """Encrypts a message using DES with different modes.

  Args:
      message: The message to encrypt (string).
      key: The 64-bit key (string).
      mode: The mode of operation (ECB, CBC, CFB).
      iv: Initialization vector (64-bit string, required for CBC mode).

  Returns:
      The encrypted message (string of hex digits).
  """
  padded_message = pad_message(message)
  blocks = [padded_message[i:i+64] for i in range(0, len(padded_message), 64)]
  ciphertext = ""

  if mode == "ECB":
    for block in blocks:
      ciphertext += des_block_encrypt(block, key)
  elif mode == "CBC":
    if not iv:
      raise ValueError("CBC mode requires an initialization vector (IV)")
    prev_block = iv
    for block in blocks:
      xor_block = xor_strings(block, prev_block)
      ciphertext += des_block_encrypt(xor_block, key)
      prev_block = ciphertext[-64:]
  elif mode == "CFB":
    if not iv:
      raise ValueError("CFB mode requires an initialization vector (IV)")
    shift_register = iv
    for block in blocks:
      keystream = des_block_encrypt(shift_register, key)
      xor_block = xor_strings(block, keystream)
      ciphertext += xor_block
      shift_register = xor_strings(keystream[:64], block)
  else:
    raise ValueError("Invalid mode of operation")

  return ciphertext.upper()

def des_decrypt(ciphertext, key, mode, iv=None):
  """Decrypts a message using DES with different modes.

  Args:
      ciphertext: The encrypted message (string of hex digits).
      key: The 64-bit key (string).
      mode: The mode of operation (ECB, CBC, CFB).
      iv: Initialization vector (64-bit string, required for CBC mode).

  Returns:
      The decrypted message (string).
  """
  blocks = [ciphertext[i:i+64] for i in range(0, len(ciphertext), 64)]
  plaintext = ""

  if mode == "ECB":
    for block in blocks:
      plaintext += des_block_decrypt(block, key)
  elif mode == "CBC":
    if not iv:
      raise ValueError("CBC mode requires an initialization vector (IV)")
    prev_block = iv
    for block in blocks:
      decrypted_block = des_block_decrypt(block, key)
      plaintext += xor_strings(decrypted_block, prev_block)
      prev_block = ciphertext[:64]
  elif mode == "CFB":
    if not iv:
      raise ValueError("CFB mode requires an initialization vector (IV)")
    shift_register = iv
    for block in blocks:
      keystream = des_block_encrypt(shift_register, key)
      xor_block = xor_strings(keystream, block)
      plaintext += xor_block
      shift_register = xor_strings(keystream[:64], block)
  else:
    raise ValueError("Invalid mode of operation")

  return unpad_message(plaintext)

# Implement DES block encryption and decryption functions (omitted for brevity)

def xor_strings(a, b):
  """Performs XOR operation on two binary strings."""
  result = ""
  for i in range(len(a)):
    result += str(int(a[i]) ^ int(b[i]))
  return result

def pad_message(message):
  """Pads the message with PKCS#7 padding."""
  pad_len = 8 - (len(message) % 8)
  return message + pad_len * chr(pad_len)

def unpad_message(message):
  """Removes PKCS#7 padding from the message."""
  pad_len = ord(message[-1])
  return message[:-pad_len]

# Example usage
message = "This is a secret message!"
key = "1010101010101010"

