import random
print("welcome to the unique password generator")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
unq_letters=int(input("how many letters u want to insert ?\n"))
unq_numbers=int(input("how many numbers u want to insert ?\n"))
unq_symbols=int(input("how many symbols u want to insert ?\n"))

password=""
for char in range(1, unq_letters + 1):
    rand_char=random.choice(letters)
    password += rand_char


for char in range(1, unq_numbers + 1):
    rand_char=random.choice(numbers)
    password += rand_char



    for char in range(1, unq_symbols + 1):
        rand_char=random.choice(symbols)
        password += rand_char
print(password)
