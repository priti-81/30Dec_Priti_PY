c=[]
for a in input('enter numbers: ').split(','):
    c.append(int(a))
c.sort(reverse=True)
print(c[-2])
# or    
b=sorted(c,reverse=True)
print(b[-2])
