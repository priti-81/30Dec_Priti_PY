def divisor(n):
    sum=0
    for a in range(1,n+1):
        if n%a==0 and a!=n:
            sum+=a
            print(a,end=' ',)   
    print ('\nTotal of divisors: ',sum)

divisor(12)
# or ******************
def divisor(n):
    
    l=[]
    for a in range(1,n+1):
        if n%a==0 and a!=n:
            l.append(a)
    print('list of all divisors',*l)    
    print(f'sum of all divisors of {n} is: ',sum(l))

divisor(12)
   