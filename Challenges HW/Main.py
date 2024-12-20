class Comp:
    def __init__(self,n):
      self.n=n
    def __lt__(self,num):
       if(self.n>num.n):
          return "ob1 is greater than ob2"
       else:
          return "ob2 is greater than ob1 " 
ob1=Comp(input("Enter any number"))            
ob2=Comp(input("Enter any number"))
print(ob1<ob2)