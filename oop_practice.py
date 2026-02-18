##class point:
##    a=1
##    b=2
##    c=3
##ob1=point()
##ob2=point()

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
        return 'phone number is updated'
    def display(self):
        print(self.name,self.age,self.sal,self.phno,self.gmail)
        print(self.__dict__)
    @classmethod
    def cls_data(cls):
        print(cls.name,cls.ceo)
    @classmethod
    def ch_ceo(cls,new_ceo):
        cls.ceo=new_ceo
        return "ceo is updated"
    @staticmethod
    def greet():
        print('welcome to apple')

e1=company("shraddha",22,608000,9898989898,"kahipan")
e2=company("dhairya",18,68900,99999999,"fomatnhidilay")
e3=company("dhrishti",20,44000,129090909,"phpnasach")


class ATM:
    service_charge=1
    def __init__(self,name,acc_no,pincode,phno,balance):
        self.name=name
        self.acc_no=acc_no
        self.pincode=pincode
        self.phno=phno
        self.balance=balance
        self.transaction=[]
        self.ATM_use=0
        self.transaction.append(f'initial balance is {balance}')

    def ser_charge(self):
        if self.ATM_use>=3:
            self.balance-=self.__class__.service_charge
        else:
            self.ATM_use+=1
        
    def deposite(self,amount):
        if amount<0:
            raise ValueError("Amount should br greater than zero")
        self.balance+=amount
        self.transaction.append(f'{amount} is credited to your account')
        self.ser_charge()

    def withdraw(self,amount):
        if amount>self.balance:
            raise valueError("Insufficient balance")
        self.balance-=amount
        self.transaction.append(f"{amount} is debited from your account")

    def transfer(self,rev_account,amount):
        self.withdraw(amount)
        rev_account.deposite(amount)
        self.transaction.append("amount is NEFT from your account")
        rev_account.transaction.append("Amount is NEFT to your account")

    def statement(self):
        for transaction in self.transaction:
            print(transaction)
        print('*'*30)
        print(f'current balance is {self.balance}')



c1=ATM('steve jobs','Bank9988',2255,698575869,1000)
c2=ATM('bill gates','Bank8877',9900,895762859,2000)


class SBI_ATM(ATM):
    service_charge=2
    def __init__(self,name,acc_no,pincode,phno,balance,gmail):
        super().__init__(name,acc_no,pincode,phno,balance)
        self.gmail=gmail

    def withdraw(self,amount):
        if amount<100:
            raise valueError("you can withdraw minimum from rs 100")
        super().withdraw(amount)


s1=SBI_ATM("Ram","sbi123",1258,584957854,1000,"kahipnmail")
s2=SBI_ATM("somu","sbi783",1908,98453454,6700,"kaysuchatnhi")
































