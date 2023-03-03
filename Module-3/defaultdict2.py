from collections import defaultdict
s= [{'gfg' : [1, 5, 6, 7], 'good' : [9, 6, 2, 10],'CS' : [4, 5, 6]},
             {'gfg' : [5, 6, 7, 8], 'CS' : [5, 7, 10]},
             {'gfg' : [7, 5], 'best' : [5, 7]}]
""" d=defaultdict(list)

for list in s:
    for key,value in list.items():
             d[key].extend(value)
print(d) """
d=dict()
for list in s:
    for a in list:
            if a in d:
                d[a]+=list[a]
            else:
                 d[a]=list[a]
print(d)