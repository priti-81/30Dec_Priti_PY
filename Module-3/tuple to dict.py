'''a=(10,'mango'),(30,'banana')
d=dict(a)
print(d)'''
a=tuple(input('enter value:').split(','))
b=tuple(input('enter names: ').split(','))
d1={key:value for key,value in zip(a,b)}
print(d1)
for a1,a2 in d1.items():
    print(a1,a2)
