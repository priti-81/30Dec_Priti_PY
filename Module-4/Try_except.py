# code for multiple exception
try:
    name = 5
    name += 5
except (NameError, TypeError) as error:
    print(error)
finally :
    print('hello')

# or>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
try:
    name = 'Bob'
    name += 5
except NameError:
    print('error')
except TypeError:
    print('can only concatenate str to str')

#or>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
try:
    name = 'Bob'
    name += 5
except Exception:
    print("concatenate str to str")


