""" rules={
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five"
}


def key(k):
    return rules.get(k,"unknown")

print(rules.get(7,"not there")) 


#print(key(5))


"""
p='piuygmail.com'
n="kjhk"
r='rakesh'
s=[p,n,r]
print("" in s)
