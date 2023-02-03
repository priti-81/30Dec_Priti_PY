'''a=['my','name','is','priti']
n=input('enter a list: ').split(' ')
if set(a).issubset(set(n)):
    print(True)
else:
    print(False)'''
    
a=['my','name','is','priti']
n=input('enter a list: ').split(' ')
if (all(x in n for x in a)):
    print(True)
    
