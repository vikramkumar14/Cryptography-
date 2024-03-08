def vigenere_encrypt(plaintext, key):
  ciphertext = ""
  j = 0
  for i in range(len(plaintext)):
    shift = ord(key[j % len(key)]) - ord('A')
    new_char = chr((ord(plaintext[i]) - ord('A') + shift) % 26 + ord('A'))
    ciphertext += new_char
    j += 1
  return ciphertext

def vigenere_decrypt(ciphertext, key):
  plaintext = ""
  j = 0
  for i in range(len(ciphertext)):
    shift = ord(key[j % len(key)]) - ord('A')
    new_char = chr((ord(ciphertext[i]) - ord('A') - shift) % 26 + ord('A'))
    plaintext += new_char
    j += 1
  return plaintext
plaintext = input("Enter plain text : ")
key = input("Enter key : ")

ciphertext = vigenere_encrypt(plaintext, key)
print(f"Encrypted message: {ciphertext}")

decrypted_text = vigenere_decrypt(ciphertext, key)
print(f"Decrypted message: {decrypted_text}")