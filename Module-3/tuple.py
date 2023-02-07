'''n=tuple(input('enter a number: ').split(','))
n1= 'mango',
print(set(n1).issubset(set(n)))'''
#or*************************************************
a='mango',
n=tuple(input('enter a number: ').split(','))
print(n)
if(all(s1 in n  for s1 in a)):
    print(True)
else:
    print(False)