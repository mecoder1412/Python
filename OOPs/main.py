class animal:
    def __init__(self,mtype,sound):
        self.type=mtype
        self.sound=sound
    def display(self):
        return self.type+" "+self.sound
lion=animal("lion","roars") 
print(lion.display())
dog=animal("dog","barks")
print(dog.display()) 
        
class vehicle:
    def __init__(self,mtype,engine):
        self.type=mtype
        self.engine=engine
    def display(self):
        return self.type+" runs on "+self.engine
Tesla=vehicle("Tesla","battery") 
print(Tesla.display())
porche=vehicle("porche","petrol")
print(porche.display()) 
del porche
print(porche.display()) 