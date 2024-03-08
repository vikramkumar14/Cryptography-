def Decrypt_encrypt(text,s):
    result = ""
    # traverse text
    for i in range(len(text)):
        char = text[i]
        if(char.isspace()):
            continue
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result
#check the above function
text = input("Enter plain text wihtout spaces : ")
text=text.lower()
key=int(input("Enter key : "))
ct=Decrypt_encrypt(text,key)
print("Text : " + text)
print("Key : " ,key)
print("Cipher: " + ct)
print("Plain Text : "+Decrypt_encrypt(ct,26-key))