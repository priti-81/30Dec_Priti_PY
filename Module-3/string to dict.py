a='w3resource'
""" from collections import Counter
print(Counter(a))  """
d={}
for a1 in a:
    l=a.count(a1)
    #d.update({a1:l})
    d[a1]=l
print(d)