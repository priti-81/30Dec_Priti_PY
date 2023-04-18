#Method overriding
class Add:
    def result(self,x,y):
        print('Addition:',x+y)

class Multi(Add):
    def result(self,a,b):
        super().result(8,8)
        print('Multiplication:',a*b)

m=Multi()
m.result(5,2)

# constructer overriding

class Father:
    def __init__(self,m):
        self.money=m
        print('father class constructer')
        print(self.money)

    def show(self):
        print('Father class instance method')

class Son(Father):
    def __init__(self,r):
        self.money=r
        print('son class constructer')
        print(self.money)
        super().__init__(3000)

    def display(self):
        print('son class instance method')

s=Son(2000)
