class Father:
    def __init__(self,name,job):
        self.name=name
        self.job=job
    def details(self):
        return "My father's name is"+self.name+"and he is working in"+self.job
class imani(Father):
    def __init__(self,name,job,name1,job1):
        super().__init__(name,job)
        self.name1=name1
        self.job1=job1
    def details(self):
        print(super().details())
        return "My name is"+self.name1+"and I am working as"+self.job1 
     
obj=imani("Patrick","cybersecurity","Imani","Baker")

print(obj.details())


