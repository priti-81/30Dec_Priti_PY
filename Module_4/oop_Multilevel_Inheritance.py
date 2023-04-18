class Mario:
    def run(self):
        print('running speed of Mario is:',15,'KM/hr')

class Supermario(Mario):
    def run(self):
        super().run()
        print('running speed of Supermario is:',30,'KM/hr')

class Supermaxmario(Supermario):
    def run(self):
        super().run()
        print('running speed of Supermaxmario is:',45,'KM/hr')

mario=Supermaxmario()
mario.run()
