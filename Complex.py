class Complex:
    def __init__(self,real=0,img=0):
        self.real = real
        self.img = img
    def __repr__(self):
        return(("%0.2f+(%0.2fj)")%(self.real,self.img))
    def __add__(self,two):
        tem=Complex()
        tem.real=self.real+two.real
        tem.img=self.img+two.img
        return tem
    def __sub__(self,two):
        tem1=Complex()
        tem1.real=self.real-two.real
        tem1.img=self.img-two.img
        return(tem1)
    def __mul__(self,two):
        tem3=Complex()
        tem3.real=((self.real*two.real)-(self.img*two.img))
        tem3.img=((self.img*two.real)+(self.real*two.img))
        return(tem3)
    def __truediv__(self,two):
        conj=Complex(two.real,-two.img)
        denominatorRes=two*conj
        denominator = denominatorRes.real
        numerator=self*conj
        return Complex(numerator.real/denominator, numerator.img/denominator)
        
C=Complex(2,3)
D=Complex(4,6)
E=Complex(4,1)
res=C+D+E
print("Addition of three complex numbers:",res)
res1=C-D
print("Subtraction of three complex numbers:",res1)
res2=E*D*E
print('Multiplication of the two numbers is:',res2)
res3=C/D/E
print('Division of two numbers is:',res3)




