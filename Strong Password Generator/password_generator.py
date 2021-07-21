import random
import string
len=input("Enter the length of the password you want to generate : ")
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(int(len)))
print("Password generated:", password)