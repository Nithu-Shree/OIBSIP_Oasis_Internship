import string
import random


# Function to generate random passwords based on user choice
def switch(choice):
    match choice:
        case 1:
            for char in range(1, len + 1):
                pwd_list.append(random.choice(string.ascii_letters+string.digits))
        case 2:
                for char in range(1, len + 1):
                    pwd_list.append(random.choice(string.ascii_letters+string.digits))
        case 3:
            
                for char in range(1, len + 1):
                        pwd_list.append(random.choice(string.ascii_letters+string.digits+string.punctuation))
        

                random.shuffle(pwd_list)

# Welcome message and user input
print("=" * 45)  # Line separator
print("\t     \033[1m🔐 CrypticPassGen 🔐\033[0m")
print("=" * 45)  # Line separator
print("Generate a Random Password")
print("-" * 45)  # Line separator
len = int(input("📏Desired password length: "))
print("-" * 45)  # Line separator
print("🔒 Select from the choices below")
print("-" * 45)  # Line separator
choice = int(input("\n1️⃣ Password with only letters\n2️⃣ Password with Letters and Numbers\n3️⃣ Password with letters, numbers, and symbols\n"))

# Initialize password list
pwd_list = []

# Generate password based on user choice
switch(choice)

# Combine the password list into a string
pwd = ''.join(pwd_list)

# Output the generated password
print("\n✨ Generated password is:", pwd)
print("\nSuccessfully generated a Secure Password!🌟")
