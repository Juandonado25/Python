caesar_cipher_art = """
  _____                               _____ _       _               
 / ____|                             / ____(_)     | |              
| |     __ _  ___  ___   __ _ _ __   | |    _ _ __ | |__   ___ _ __ 
| |    / _` |/ _ \/ __| / _` | '__|  | |   | | '_ \| '_ \ / _ \ '__|
| |___| (_| |  __/\__ \| (_| | |     |_____| | |_) | | | |  __/ |   
 \_____\__,_|\___||___/ \__,_|_|     \_____|_| .__/|_| |_|\___|_|   
                                             | |                    
                                             |_|                    
"""
print(caesar_cipher_art)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text,shift):
    text_encrypted = ""
    for letter in text:
        if letter in alphabet:
            i = alphabet.index(letter)+shift
            if i>25:
                i -= 26
                text_encrypted += alphabet[i]
            else:
                text_encrypted += alphabet[i]
        else:
            text_encrypted += letter
    print(f"The encrypted text is '{text_encrypted}'.")

def decrypt(text,shift):
    text_decrypted = ""
    for letter in text:
        if letter in alphabet:
            i = alphabet.index(letter)-shift
            if i < 0:
                i += 26
                text_decrypted += alphabet[i]
            else:
                text_decrypted += alphabet[i]
        else:
            text_decrypted += letter                
    print(f"The decrypted text is '{text_decrypted}'.")

def caesar(direction):
    if direction=="encode":
        encrypt(text,shift)
    elif direction=="decode":
        decrypt(text,shift)

ok = True
while ok:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    if direction=="encode" or direction=="decode":
        text = input("Type your message: ").lower()
        shift = int(input("Type the shift number: "))
        caesar(direction)
    else:
            print("invalid input.")
    user_input = input("Type 'yes' if you want to go again. Otherwise type 'no': ")
    if user_input=="no":
        ok = False
