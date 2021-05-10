import sys

class Customer:
    "Customer class with bank related Operations"
    bankName = "HDFC Bank"

    def __init__(self,name,AccNo,balance=0):
        self.name=name
        self.AccNo = AccNo
        self.balance = balance
    
    def getBalance(self):
        print("Balance is Rs.",self.balance)

    def deposit(self,amount):
        self.balance = self.balance+amount
    
    def withdraw(self,amount):
        if amount > self.balance:
            print("Amount is greater than balance --- Insufficient funds")
            sys.exit(0)
        else:
            self.balance = self.balance - amount
    
if __name__ == "__main__":
    cust = Customer("Manoj","0950",10)
    cust.getBalance()
    cust.deposit(195)
    cust.getBalance()
    cust.withdraw(80)
    cust.getBalance()
    cust.withdraw(155)
    

