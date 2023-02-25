d1 = {'c': 500, 'b': 300, 'a':100,'d':450}
d2 = {'a': 300, 'b': 200,'d':200,'f':525}

for key in d2:
    if key in d1:
        d2[key]=d1[key]+d2[key]
    else:
        d1.update(d2)
print(d1)    