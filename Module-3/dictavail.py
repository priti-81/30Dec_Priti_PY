#using if and in operator
a={102:'mango',101:'banana'}
i=int(input('enter key u want to cheak: '))
'''if i in a:
    print('it is present')
else:
    print(i,'key not present')'''
#using in built method
'''if a.get(i)==None:
    print('no value')
else:
    print('value is:',a.get(i))'''
#using in built method
if i in a.keys():
    print(i,'is present')
else:
    print(i,'is not present')