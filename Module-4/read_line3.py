f=open('D:/py.txt','r')
list1=""
for line in f:
    line=line.strip('\n')
    list1+=line
    
f.close()
print(list1)