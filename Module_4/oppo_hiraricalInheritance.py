class Hero:
    def kick(self):
        print('Hero kicked')

class Superhero(Hero):
    def kick(self):
        print('Superhero kicked')

class Badhero(Hero):
    def kick(self):
        print('Badhero kicked')


hero=Superhero()
hero.kick()

bhero=Badhero()
bhero.kick()