#Write a Python program that takes two lists and returns true if they have at least one common member.
a=set(([x for x in input('enter any list: ').split(',')]))
b=set(([x for x in input('enter any list: ').split(',')]))
print(True) if (a.intersection(b)) else print(False)

#find common element in two set without intersection method
a=set(([x for x in input('enter any list: ').split(',')]))
b=set(([x for x in input('enter any list: ').split(',')]))
c=[]
for a1 in a:
    if a1 in b:
        c.append(a1)
for item in c:
    print(item)
