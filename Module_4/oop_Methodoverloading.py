# Method overloading

class Mario:
    x=10
    def run(self,s):
        print('speed of mario is:',s,'km/hr')

    def run(self,*a): # last function called use arbitary or default parameter
        print('increased speed of mario is:',Mario.x)

m=Mario()
m.run()