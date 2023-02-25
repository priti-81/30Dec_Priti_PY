from collections import Counter
s =[{'item': 'item1', 'amount': 400},{'item': 'item2', 'amount': 
300},{'item': 'item1', 'amount': 750}]
'''result=Counter()
for d in s:
    print(d)
    result[d['item']]+=d['amount']
print(result)'''
# without Counter function*******************
res=dict()
for a in s:
    for a1 in a:
        if a1=='amount':
            pass
        else:
            if a[a1] not in res:
                res[a[a1]]=a['amount']
            else:
                res[a[a1]]+=a['amount']
print(res)