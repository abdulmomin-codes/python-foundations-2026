#Build a BankAccount class. It should initialize with account_holder (str) and 
#balance (float, default 0.0).
# Implement instance methods deposit(amount) and withdraw(amount) with validation
# (cannot withdraw more than current balance, cannot deposit negative amounts).
 #Add a __str__ method returning "Account [holder]: Balance $X.XX".
 

class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance
     
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f'Amount: ${amount} deposited'
        else:
            return 'Negative balance'
         
    def withdraw(self, amount):
        if amount > self.balance:
            return f'Cant withdraw more than {self.balance}'
        else:
            self.balance -= amount
            return f'Withdrawal of ${amount}'
                

    def __str__(self):
        return f'Account {self.account_holder}: Balance ${self.balance:.2f}'       
        
          
acc1 = BankAccount('Alex', 30000)
print(acc1.withdraw(20000))
print(acc1.deposit(5000))
print(acc1)