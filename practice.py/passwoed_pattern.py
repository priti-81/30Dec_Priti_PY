import re

n1=input('Enter password: ')

#up='#TR1kjl23'
user=r"^(?=.*[A-Z])(?=.*[@$!%*#?&])(?=.*\d).{8,12}$"

user_pattern=re.compile(user)
si=re.findall(user_pattern,n1)
# print(si)
# print([n1])
if [n1]==si:
     if [n:=input('Enter confirm password: ')]==[n1]:
        print('\npassword generated successfully')    
else:
    print('password should have atleast one small,capital,digit,special character' 
          'and min 8-max 12 length required')
    
 