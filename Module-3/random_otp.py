import math
from random import random
"""def generateOTP():
    digits='0123456789'
    otp=""
    for i in range(4):
        otp+=digits[math.floor(random()*10)]
    return otp

print(generateOTP()) """
#6 digit capcha****************************
""" def generateOTP():
    string='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    otp=""
    length=len(string)
    for i in range(6):
        otp+=string[math.floor(random()*length)]
    return otp
print(generateOTP()) """
# capcha using string constants**********************
import string,random

def rand_pass(size):
    generate_pass=''.join([random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits)
                           for n in range(size)])
    return generate_pass

print(rand_pass(6))