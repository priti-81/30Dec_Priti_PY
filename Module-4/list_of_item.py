items = ['Table ', 'Chair ', 'Mirror ', 'Curtain ', 'Almirah ']
""" file = open('D:/items.txt','w')
file.writelines(items)
file.close()
 """
#or with open.......
with open('D:/items.txt','w') as t:
	t.write(''.join(items))