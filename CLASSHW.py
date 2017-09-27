class Bank(object):
    def __init__(self, Name, Accno, balance=500):
        self.Name = 'nirmal'
        self.Accno = Accno
        self.balance = balance
    def deposit(self,Amount):
        self.Amount=Amount
        self.balance=self.balance+Amount
        return self.balance
    def Withdraw(self,Money):
        self.Money=Money
        self.balance=self.balance-Money
        return self.balance
    def display(self):
       print("""The details of the customer is
              a.Name- %s
              b.Balance - %d"""%(self.Name,self.balance))
while True:
    print("1.Enter your details\n2.Deposit Money\n3.Withdraw\n4.Display\n5.Exit")
    Option=int(input("Enter what you would like to do"))
    if(Option==1):
         getname=input("Enter Name:")
         getaccno=int(input("Enter Accno:"))
         B=Bank(getname,getaccno,500)
    if(Option==2):
        getamount=int(input("enter the money to deposit"))
        B.deposit(getamount)
    if(Option==3):
        getmoney=int(input("Enter money to withdraw"))
        B.Withdraw(getmoney)
    if(Option==4):
        B.display()
    if(Option==5):
        break      
