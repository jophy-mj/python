class bank:
    def __init__(self):
        self.balance = 0
        self.acno=input("Enter your A/C NO:")
        self.name=input("Enter your name:")
        self.actype=input("Enter your A/C type:")
    def deposit(self):
        amt=float(input("Enter amount to deposite:"))
        self.balance=self.balance+amt
        print("Amount deposited:",amt)
    def withdraw(self):
        amnt =float(input("Enter amount to withdraw:"))
        self.balance=self.balance-amnt
        print("You withdraw:",amnt)
    def dis(self):
        print(self.name," available net balance is:",self.balance)
bank1=bank()
n=input("DEPOSITE or WITHDRAW")
if n=="DEPOSITE" or n=="deposite":
    bank1.deposit()
else:
    bank1.withdraw()
bank1.dis()
