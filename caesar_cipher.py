alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text,shift):
    text_encrypted = ""
    for letter in text:
        i = alphabet.index(letter)+shift
        if i>25:
            i -= 26
            text_encrypted += alphabet[i]
        else:
            text_encrypted += alphabet[i]
    print(f"The encrypted text is '{text_encrypted}'.")

def decrypt(text,shift):
    text_decrypted = ""
    for letter in text:
        i = alphabet.index(letter)-shift
        if i < 0:
            i += 26
            text_decrypted += alphabet[i]
        else:
            text_decrypted += alphabet[i]
    print(f"The decrypted text is '{text_decrypted}'.")

def caesar(direction):
    if direction=="encode":
        encrypt(text,shift)
    elif direction=="decode":
        decrypt(text,shift)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
if direction=="encode" or direction=="decode":
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    caesar(direction)
else:
        print("invalid input.")
        
