#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
let = int(input("How many letters would you like in your password?\n")) 
sym = int(input(f"How many symbols would you like?\n"))
num = int(input(f"How many numbers would you like?\n"))

#EASY LEVEL:
    
password = ""
for i in range(1, let+1):
    rand_let = random.choice(letters)
    password = password + rand_let

for i in range(1, sym+1):
    rand_sym = random.choice(symbols)
    password = password + rand_sym

for i in range(1, num+1):
    rand_num = random.choice(numbers)
    password = password + rand_num

print(password)

#HARD LEVEL
#we will have to shuffle the whole thing of above. Hence we need everything in the form of lists

password = []
for i in range(1, let+1):
    rand_let = random.choice(letters)
    password.append(rand_let)

for i in range(1, sym+1):
    rand_sym = random.choice(symbols)
    password.append(rand_sym)

for i in range(1, num+1):
    rand_num = random.choice(numbers)
    password.append(rand_num)

print(password)
random.shuffle(password)
pas = "".join(password)
print(pas)