""" def test_range(n):
   print(f"{n} is in range") if n in range(1,11) else print(f"{n} is out of range")
test_range(5)"""
#*******************************************
""" list=[]
n=int(input('enter a number: '))
for a in range(2,n+1):
   if (n%a==0):
       list.append((n//a))
#print(list)
sum1=0
for a1 in list:
    sum1=sum1+a1
#print(sum1)
if n==sum1:
    print(n,'is a perfect number')
else:
    print(n,'is not perfect number') """
#*************************************************
def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
print(perfect_number(6))

 