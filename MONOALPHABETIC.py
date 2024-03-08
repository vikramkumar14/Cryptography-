def monoalphabetic_cipher(plaintext, key):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  ciphertext = ""
  for char in plaintext.lower():
    if char in alphabet:
      index = alphabet.index(char)
      new_char = key[index]
      ciphertext += new_char
    else:
      ciphertext += char
  return ciphertext

# Example usage
plaintext = "cab"
key = "pqr"
ciphertext = monoalphabetic_cipher(plaintext, key)
print(ciphertext)