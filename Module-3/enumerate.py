d={'1': ['a','b'], '2': ['c','d']}
#res=[(x,y) for idx,x in enumerate(d1) for y in d1[idx+1: ]]
#print(res)
""" from itertools import combinations
res=list(combinations(d1,2))
print(res) """
""" for j in range(len(d.values())):
        for a in range(len(d.values())):
            print(d['1'][j]+d['2'][a],end=' ') """

for j,k in d.items():
    #print(j,k)
    for a in k:
        
        nindex=list(d.keys()).index(j)
        #print(nindex)
        if(nindex<len(d)-1):
            nkey=list(d.keys())[nindex+1]
           # print(nkey)
            res=map(lambda i:a+i,d[nkey])
            print(list(res))
            #print(a+d[nkey][k.index(a)])
        #print(a+d.keys())
        print(d['1'][j]+d['2'][a],end=' ')
        