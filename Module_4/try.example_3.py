# program to print the reciprocal of even numbers

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0,print('not an even no.')
except:
    pass
    #print("Not an even number!")
else:
    try:
        reciprocal = 1/num
        print(reciprocal)
    except ZeroDivisionError as e:
        print(e)