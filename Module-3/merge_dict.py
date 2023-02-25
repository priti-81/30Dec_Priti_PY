a={'apple':100,'banana':70}
b={'chiku':80,'guvava':120}
from collections import ChainMap
print(ChainMap(a,b))
#or.............
a.update(b)
print(a)
#or..................
print({**a,**b})