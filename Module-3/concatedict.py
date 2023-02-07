'''d=list({101:'mango',102:'papaya'})
d1=list({10:'rakesh',20:'rohan'})
print(d+d1)'''
#concatnate two dictionary user input
a=input('enter values: ').split(',')
a1=input('enter names: ').split(',')
d=dict()
for key,value in zip(a,a1):
      d.setdefault(key,value)
print(d)
i1=input('enter values for add: ').split(',')
i2=input('enter names for add: ').split(',')
dict={key1:value2 for key1,value2 in zip(i1,i2)}
d.update(dict)
print(d)

