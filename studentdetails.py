class Person:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

class student(Person):

    def __init__(self, fname, lname, year):

        super().__init__(fname, lname)
        self.graduationyear = year

Mina = student("Mina", "Raju", 2007)

Mina.printname()
print(Mina.graduationyear)
        
