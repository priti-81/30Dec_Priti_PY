s =[{'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}]
""" res=dict()
for a in s:
    for a1 in a:
        if (a1=='item'):
            if a[a1] in res:
                res[a['item']]+=a['amount']
            else:
                res[a['item']]=a['amount']
print(res) """
from collections import defaultdict
d=defaultdict(int)
for a in s:
    for a1 in a:
            if a1=='item':
                d[a['item']]+=a['amount']
print(d)