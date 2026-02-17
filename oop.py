class company:
    cname="apple"
    ceo="steve jobs"
    def __init__(self,name,age,sal,phno,gmail):
        self.name=name
        self.age=age
        self.sal=sal
        self.phno=phno
        self.gmail=gmail
    def ch_phno(self,new_phno):
        self.phno=new_phno
        return "phone number is updated"
    def display(self):
        print(self.name,self.age,self.sal,self.phno,self.gmail)
        print(self.__dict__)
    @classmethod
    def cls_data(cls):
        print(cls.cname,cls.ceo)
    @classmethod
    def ch_ceo(cls,new_ceo):
        cls.ceo=new_ceo
        return "ceo name is updated"
    @staticmethod
    def greet():
        print("welcome to apple")



e1=company("shraddha",44,490000,4535647263,"S@gmail.com")
e2=company("shra",44,19080000,10373263,"b@gmail.com")
e3=company("rama",44,780000,6025647263,"k@gmail.com")
e4=company("dhryshti",44,8000,97653647263,"r@gmail.com")
e5=company("soniya",44,97800,987347263,"z@gmail.com")





class ATM:
    service_charge=1
    def __init__(self,name,ac_num,pincode,phno,balance):
        self.name=name
        self.ac_num=ac_num
        self.pincode=pincode
        self.phno=phno
        self.balance=balance
    def deposite(self,amount):
        pin=int(input("enter your pin:"))
        if pin !=self.pincode:
            raise valueerror("wrong pin")
        if amount<0:
            raise valueError("amount should greater than zero")
        self.balance+=amount
    def withdraw(self,amount):
        pin=int(input("enter your pin:"))
        if pin !=self.pincode:
            raise valueerror("wrong pin")
        if self.amount<amount:
            raise valueError("insufficient fund!!!")
        self.balance-=amount
    

c1=ATM("shraa","SBI2345",123,9863567382,5000)












      
