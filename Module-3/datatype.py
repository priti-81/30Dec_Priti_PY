#print(tuple([int(x) for x in input('enter a number: ').split(',')]))
#print(tuple({x for x in input('enter a string: ').split(',')}))
n=input('enter a name: ')
print(tuple(n for e in range(0,5)))