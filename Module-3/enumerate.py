d={'1': ['a','b'], '2': ['c','d']}

""" from itertools import combinations
res=list(combinations(d1,2))
print(res) """
# dynamic solution
l=list(d.keys())
sum=[]
for j in range(len(list(d[l[0]]))):
        for a in range(len(d[l[0]])):
            sum.append(d[l[0]][j]+d[l[1]][a])
print(*sum)   
            

#dynamic solution
""" for j,k in d.items():
    #print(j,k)
    for a in k:
        
        nindex=list(d.keys()).index(j)
        #print(nindex)
        if(nindex<len(d)-1):
            nkey=list(d.keys())[nindex+1]
            #print(nkey)
            res=map(lambda i:a+i,d[nkey])
            print(*res)
             """