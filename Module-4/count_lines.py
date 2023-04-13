f=open('D:/py.txt','r')
no_of_lines=0
for line in f:
    no_of_lines+=1
f.close()
print(no_of_lines)
