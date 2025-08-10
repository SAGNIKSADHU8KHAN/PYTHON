class computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling price of the computer is {}".format(self.__maxprice))

    def setmaxprice(self, price):
        self.__maxprice = price 

comp = computer()

comp.sell()

comp.__maxprice = 1000
comp.sell()

comp.setmaxprice(1200)
comp.sell()

    