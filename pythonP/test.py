import random
import string

char = (string.ascii_letters+string.ascii_lowercase+string.ascii_uppercase+string.digits)

password = ''
length = int(input ( 'enter the length of your password : '))

for _ in range(length):
    characters = random.choice(char)
    password+=characters
    
print(f"your password is {password}")