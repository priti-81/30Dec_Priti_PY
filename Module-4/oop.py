class Product:
    def __init__(self):
        self.model='Realmex'

    @staticmethod
    def show_model(p):
        print(p)

pr=Product()
pr.show_model(10)