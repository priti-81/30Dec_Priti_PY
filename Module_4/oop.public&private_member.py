class Product:
    def __init__(self,name):
        self.name=name # public member use outside the class through create class object
        self.__price=100 # private member use inside the class

    def details(self):
        print('name:',self.name)
        print('price:',self.__price)
        print('after discount price is:',self.__caldis())

    def __caldis(self):
        return self.__price - 10
    

parle=Product('parle')
print(parle.name)
parle.details()

parle.name='parle-G'
parle.details()
