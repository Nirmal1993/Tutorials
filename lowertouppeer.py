class lowertoupper():
    def __init__(self,string):
        self.string=string
    def uptolow(self,string):
        string=string.upper()
        print(string)
string=input("Enter string:")
LUP=lowertoupper(string)
LUP.uptolow(string)

