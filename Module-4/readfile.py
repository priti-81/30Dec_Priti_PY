f=open('D:/py.txt','r')
import os
print(f.read())
print(f.seek(0))
print(os.stat("D:/py.txt").st_size)
print(f.readlines())
f.close()

 
