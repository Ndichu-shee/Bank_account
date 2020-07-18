class BankAccount:
    bank ="KCB"
    
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0
    def account_name(self):
        name ="{} account for {} {}".format(self.bank,self.first_name,self.last_name)
        return name
    
    def  deposit(self,amount):
        self.balance += amount
        if amount>0:
            print("You can deposit the money")
        else:
            print("Sorry you can't deposit that amount of money")
        print("You have deposited {} to your acccount".format(amount)) 
        
    def get_balance(self):
        return "The balance for {} is {} ".format(self.account_name(),self.balance)
    
    def withdraw(self,amount):
        amount=0
        if self.balance>=amount:
            self.balance -= amount
            print("You can withdraw the money")
        else:
            print("You have no money left in you account")
        print("You have withdrawn {} from your account".format(amount))
        
    def check_balance(self):
        return "The instant balance for {} is {} ".format(self.account_name(),self.balance)
    
acc1 = BankAccount("Joyce","Ndichu")
acc2 = BankAccount("Mary","Jude")

acc1.deposit(100)
acc2.deposit(60)
acc1.deposit(5)
acc2.deposit(100)

acc1.withdraw(10)
acc2.withdraw(30)

print(acc2.get_balance())
print(acc1.get_balance())
acc3 = BankAccount("Joy","Nal")
acc4 = BankAccount("Mar","Jade")
acc3.deposit(5)
acc4.deposit(100)
acc3.withdraw(10)
acc4.withdraw(20)
print(acc3.check_balance())
print(acc4.check_balance())