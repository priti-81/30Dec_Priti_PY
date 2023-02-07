a=tuple(input('enter value:').split(','))
b=tuple(input('enter names: ').split(','))
d1={key:value for key,value in zip(a,b)}
print(d1)
print(sorted(d1.keys()))
print(sorted(d1.items(),reverse=True))