class add:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        print("addition is %0.2f"%(self.a+self.b))
    #def addition(self):
    #    return (self.a+self.b)
    
A=add(2,3)
A.__str__()
