'''for x in input('enter a name: ').split(','):
    s1=''.join(x)
    print(s1,end='')'''
print(','.join(tuple( x for x in input('enter a name: ').split(','))))
