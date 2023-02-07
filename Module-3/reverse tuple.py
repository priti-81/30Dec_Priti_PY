l1=(tuple(input('enter a number:').split(',')))
s=reversed(l1)
s1=(tuple(s))
print(s1)
for a in reversed(l1) :
    print(a[::-1])