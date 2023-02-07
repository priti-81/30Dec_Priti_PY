n=tuple(input('enter a name: ').split(','))
for a in n:
   print(a.replace(a[-1],'*'))
   
#for a in tuple(input('enter a number: ').split(',')):
     # print(a[:-1]+'$')