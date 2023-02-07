for a in tuple(input('enter names: ').split(',')):
    for a1 in enumerate(a):
        #print(a1[0],a1[1])
        if a.count(a1[1])>1:
            if a1[0]==a.index(a1[1]):
                print('in',a,a1[1],'is repeated',a.count(a1[1]),'times')
        else:
             pass
