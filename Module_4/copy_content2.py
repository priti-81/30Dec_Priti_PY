f=open('D:/py.txt','r')
f1=open('D:/items.txt','a')
for file in f:
        f1.write(file)

f.close()
f1.close()