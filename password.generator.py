#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?: ")) 
nr_symbols = int(input(f"How many symbols would you like?: "))
nr_numbers = int(input(f"How many numbers would you like?: "))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pw = ""

for c in range(0,nr_letters):
    pw += letters[random.randint(0,nr_letters-1)]
for c in range(0,nr_numbers):
    pw += numbers[random.randint(0,nr_numbers-1)]
for c in range(0,nr_symbols):
    pw += symbols[random.randint(0,nr_symbols-1)]
print(f"Password generated (Eazy Level): {pw}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

listChar = list(pw)

for pos in range(0,len(listChar)):
    r = random.randint(0,len(listChar))
    aux = listChar[pos]
    listChar[pos] = listChar[r]
    listChar[r] = aux

pw2 = "".join(listChar)

print(f"Password generated (Hard Level): {pw2}")