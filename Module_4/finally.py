def divide(x, y):
    try:
        
        result = x // y
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
    else:
        print("Yeah ! Your answer is :", result)
    finally: 
        # this block is always executed  regardless of exception generation. 
        print('This is always executed')  
 
divide(3,2)
divide(3,0)