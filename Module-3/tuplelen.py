#length of tuple
n=(tuple(input('enter a number: ').split(',')))
print(len(n))
#or length of element of tuple
n= tuple(input('enter names: ').split(','))
for a in n:
    print(len(a))
