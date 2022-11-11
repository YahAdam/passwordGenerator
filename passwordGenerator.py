import random
import string

print("how many charactors would you like the password to be?")
passLength = input()

print("how many numbers?")
passNums = input()

print("any capital letters (y/n)?")
passCap = input()

print("any special characters? (y/n)?")
passSpecial = input()


password = ''

if (passCap == 'y'):
    password = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=int(passLength)))
elif (passCap == 'n'):
     password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=int(passLength)))
else: 
    print("password cannot be created, please check inputs")

print(password)

