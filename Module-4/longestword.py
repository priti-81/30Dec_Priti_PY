f=open('D:/py.txt','r')
line1=[]
for line in f:
    line=line.strip('\n')
    line1.append(line.split())
maximum=0
max1=[]
for a in line1:
    for a1 in a:
        if len(a1)>maximum:
            maximum=len(a1)
            max1.append(a1)
f.close()    
    
            
print('longest word in the file:',max1[-1])
print('length is:',maximum)


#or by making function........

def longest_word(filename):
    with open(filename,'r') as f:
        words=f.read().split()
    max_len=len(max(words,key=len))
    return [ (word,max_len) for word in words if len(word)==max_len]

print(longest_word('D:/py.txt'))
