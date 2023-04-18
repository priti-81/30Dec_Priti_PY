#counting of each word......
f=open('D:/py.txt','r')
d=dict()
for line in f:
    line=line.lower()
    words=line.split()
    for word in words:
        if word in d:
            d[word]+=1
        else:
            d[word]=1
for key in d.keys():
    print(f' {key} : {d[key]}')

#by counter method.....
from collections import Counter
def word_count(filename):
    with open(filename,'r') as f:
        return Counter(f.read().split())
    
print(word_count('D:/py.txt'))