d1 = {'c': 500, 'b': 300, 'a':100,'d':450}
d2 = {'a': 300, 'b': 200,'d':200,'f':525}
from collections import Counter
print(Counter(d1)+Counter(d2))