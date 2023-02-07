a=tuple(input('enter value:').split(','))
b=tuple(input('enter names: ').split(','))
d=dict()
for a1,b1 in zip(a,b):
    d.setdefault(a1,b1)
print(d)
# access the items of dictionary
for key,value in d.items():
    print(key,value)
