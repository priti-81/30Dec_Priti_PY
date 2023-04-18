#program that user to enter only odd numbers, else will raise an exception.

def oddnum():
    try:
     for a in (input('enter number:')).split(','):
        b=int(a)
        if b%2==0:
            raise Exception ('enter odd numbers only...') 
        print(b)
    except Exception as e:
        print(e)


oddnum()