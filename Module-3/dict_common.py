d1 = {'c': 500, 'b': 300, 'a':100,'d':450}
d2 = {'a': 300, 'b': 200,'d':200,'f':525}
list=[]
list1=[]
for key,value in d1.items():
    for key1,value1 in d2.items():
        if key==key1:
         list.append((key))
         list1.append((value+value1))
        
dict=dict()
for a,b in zip(list,list1):
        dict.setdefault(a,b)
       
d1.update(d2)
d1.update(dict)
print(d1)