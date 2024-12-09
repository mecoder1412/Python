diam=int(input("Enter the diameter of the circle"))

class circle:
    def __init__(self,pi,r):
        self.pi=pi
        self.r=r
    def display(self):
        return self.pi*self.r*self.r
cir1=circle(3.142,diam/2) 
print("area of the circle",cir1.display())   