'''a=['my','name','is','priti']
n=input('enter a list').split(' ')
if(all(x in n for x in a)):
    print('yes,it is in sublist')
else:
    print('no,it is not in  sublist')'''
# or*************************************

a='my name is priti'.split(' ')
n=input('enter a list').split(',')
if(all(x in n for x in a)):
     print('yes,it is in sublist')
else:
    print('no,it is not in  sublist')
