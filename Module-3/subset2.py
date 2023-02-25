a=['my','name','is','priti']
n=input('enter a list').split(' ')
if set(a).issubset(n):
    print(True)
else:
    print(False)
#print(set(a))