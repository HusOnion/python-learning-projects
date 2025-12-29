import random 
import string 

chars = string.punctuation + string.digits + string.ascii_letters + " "
chars = list(chars)

key = chars.copy()

random.shuffle(key)

text = input("Enter a message to encrypt: ")
encrypted_message = ""


for letter in text:
    index = chars.index(letter)
    encrypted_message += key[index]

print(f"original message: {text}")
print(f"encrypted message: {encrypted_message}")


ask = input("Do you want to decrypte it? (Y/N): ").upper()

if ask == "Y":
    encrypted_message = input("Enter a message to decrypt: ")
    decrypted_message= ""

    for letter in encrypted_message:
        index = key.index(letter)
        decrypted_message += chars[index]
    
    print(f"encrypted message: {encrypted_message}")
    print(f"decrypted message: {decrypted_message}")    


print("bye :)")