""" def facto(i):
    if i>0:
        n=1
        sum=1
    while n<=i:
        sum=sum*i
        i-=1
    return(sum)

a=facto(5)
print(a)"""
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1)
a=factorial(0)
print(a)

import math
 
def facto(n):
    return(math.factorial(n))
a=facto(4)
print(a)