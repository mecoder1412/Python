class word:
    def __init__(self):
        self.__name="Jianna"
    def display(self):
        print("name:{}".format(self.__name))
    def revname(self,rname):
        self.__name=rname
j=word()
j.display()
j.revname("annaiJ")
j.display()            

