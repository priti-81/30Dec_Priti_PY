a={101:'mango',102:'banana',103:'chiku',104:'gvava'}
a1=(input('enter keys you want to check: ')).split(',')
for a2 in a1:
    if int(a2) in list(a.keys()):
         print(f'{a2} is present')
    else:
        print(f'{a2} is not present')

