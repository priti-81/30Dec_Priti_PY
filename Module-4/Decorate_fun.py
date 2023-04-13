def decore(fun):
    def inner():
        a=fun()
        add=a*5
        return add
    return inner

def decore1(fun):
    def inner():
        b=fun()
        add=b+5
        return add
    return inner



def num():
    return 10

#result=decore(num)
c=decore1(decore(num))
print(c())
