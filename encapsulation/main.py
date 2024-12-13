class Computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))
    def setmaxprice(self,price):
        self.__maxprice=price
c=Computer()
c.sell()                
c.__maxprice=1000
c.sell()
c.setmaxprice(1000)
c.sell()

class word:
    def __init__(self):
        self.__name="Jiannna"
    def display(self):
        print("name:{}".format(self.__name))
    def setname(self,cname):
        self.__name=cname
n=word()
n.display()            
n.setname("Imani")
n.display()