##single level inheritance--it is a phenonmenon of deriving properties
##from single parent class to single child class.
##--since properties get derived only one time, it is known as single
##level inheritance
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

##multilevel inheritance--process of deriving the properties from
##one class to another class by considering more than one level of
##inheritance
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

class HDFC_ATM(SBI_ATM):
    service_charge=0.5

h1=HDFC_ATM("yash","hdfc1122",1265,987654545,5000,'yash@gmail.com')


##multiple inheritance-- process of deriving properties from multiple parent
##class to single child class

class mom:
    def cook(self):
        print("mom: i make delicious food")
    def rules(self):
        print("mom: be home by 9 pm")

class dad:
    def drive(self):
        print("i drive the car")
    def rules(self):
        print("ask your mom")

class child(dad,mom):
    def games(self):
        print("i just want to play games")

c1=child()
c1.games()
c1.cook()
c1.drive()
c1.rules()


##
##Hierarhical inheritance:-- process of deriving the properties from single parent
##to multiple child class


class trainer:
    def subject(self):
        print("i am a python trainer")
    def python_lecture(self):
        print("class time 1 to 3pm")

class std1(trainer):
    def hobby(self):
        print("i love sleep")

class std2(trainer):
    def hobby(self):
        print("i love drawing")
    

class std2(trainer):
    def hobby(self):
        print("i love dancing")

print("*"*30)
##Hybrid inheritance:-- combination of more than one type of inheritance

class grandfather:
    def land(self):
        print("i own 10 acres of land")

class mom:
    def cook(self):
        print("mom: i make delicious food")
    def rules(self):
        print("mom: be home by 9 pm")

class dad(grandfather):#single level inheritance
    def drive(self):
        print("i drive the car")
    def rules(self):
        print("ask your mom")

class child(dad,mom):#multilevel and multiple
    def games(self):
        print("i just want to play games")


c1=child()
c1.drive()
c1.rules()


















    






















