class personalinfo():
    def __init__(self):
        self.addr="No.22 Corinthian"
        self.pincode = '92115'
    def display(self):
        print("Address is",self.addr)
        print("pincode is",self.pincode)
Person=personalinfo("No.25 west street",92115)
Person = personalinfo()
Person.display()

    
