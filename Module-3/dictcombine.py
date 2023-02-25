a=input('enter key: ').split(',')
b=input('enter value: ').split(',')
n=len(a)
import numpy as nm
split_list=nm.array_split(b,n)

array=[]
for a1 in split_list:
    array.append(a1.tolist())

d={} 
for d1,d2 in zip(a,array):
    d.setdefault(d1,d2)
print(d)