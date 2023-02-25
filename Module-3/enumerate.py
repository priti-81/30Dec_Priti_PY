d=({'1': ['a','b'], '2': ['c','d']})
d1=list(d['1']+d['2'])
#res=[(x,y) for idx,x in enumerate(d1) for y in d1[idx+1: ]]
#print(res)
'''from itertools import combinations
res=list(combinations(d1,2))
print(res)'''
print('a'+'c','a'+'d', 'b'+'c', 'b'+'d')