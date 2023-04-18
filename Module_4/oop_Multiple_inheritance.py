class Mother:
    Mothername=1
    def mother(self):
        print(self.Mothername)

class Father:
    Fathername=2
    def father(self):
        print(self.Fathername)

class son(Mother,Father):
    def parents(self):
        super().father()
        super().mother()
        print('Fathername:',self.Fathername)
        print('Mothername:',self.Mothername)


s=son()
s.Mothername='suman'
s.Fathername='Gajanand'
s.parents()

m=Mother()
print(Mother.Mothername)
print(m.Mothername)