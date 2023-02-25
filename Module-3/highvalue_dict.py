d={1:100,2:250,3:50,4:150,5:230}
l=[]
for a in d.values():
    l.append(a)
a1=sorted(l)
print(a1[-3:])
#or**********************************
large_num=l[0]
for number in l:
    if large_num<number:
        large_num=number
print(large_num)