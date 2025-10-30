class Account:
    def __init__(self,balance,Acc):
        self.Account_no = Acc
        self.balance = balance


        # Debit method
    
    def debit(self, amount):
        self.balance -= amount
        print("Rs.",amount , "has been deducted from your account.")
        print("your current balance is :",self.balance,".Rs")

    def Credit(self, amount):
        self.balance += amount
        print("Rs.",amount , "has been credited to your account.")
        print("your current balance is :",self.balance,".Rs")

    def total_balance(self):
        return self.balance()   



acc1 = Account(10000 , 123456)
acc1.debit(1000)
acc1.Credit(2000)

acc2 = Account(20000 , 1234567)
acc2.debit(1000)
acc2.Credit(2000)