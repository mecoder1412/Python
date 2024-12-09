class Cow:
    def __init__(self,size,food):
        self.size=size
        self.food=food
    def details(self):
        return "A cow is "+self.size+" and it feeds on "+self.food
class calf(Cow):
    def __init__(self,size,food,size1,food1):
        super().__init__(size,food)
        self.size1=size1
        self.food1=food1
    def details(self):
        print(super().details())
        return "A calf is "+self.size1+" and it feeds on "+self.food1 
     
obj=calf("big","grass","small","milk")

print(obj.details())


