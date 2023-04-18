class Mobile: # Mobile is class object...
    RAM='8GB' # class object variable

    def __init__(self):
        self.model='oppo' #instance variable
    
    def f1(self,p):  #instance method
        self.price=p  # p is local variable
        print('Model:',self.model,'price:',self.price)

    @staticmethod
    def show_model(m,p):    
        print('RAM of oppoa77:',Mobile.RAM) # or t1.RAM u can access by class object also
        print('Model:',m,'price:',p)

    @classmethod # u want to change class variable
    def f3 (cls,p):
        cls.RAM=p
        print('RAM of oppo is', cls.RAM)

t1= Mobile()

t1.f1(40000)
t1.show_model('realmi',30000)
t1.f3('16GB')
 
#or by class u can call the function but no meaning why u make object..

t=Mobile()
Mobile.f1(t,40000)
Mobile.show_model('realmi',50000)
Mobile.f3('32GB')