# single inheritance

class Mario: #parent class
    def __init__(self,speed):
        self.speed=speed

    def runnig (self):
        print('speed:',self.speed)

class Supermario(Mario):# child class
    def increae_speed(self):
        self.speed=self.speed*2
        print('speed:',self.speed)

mario=Supermario(5)
mario.runnig()
mario.increae_speed()

