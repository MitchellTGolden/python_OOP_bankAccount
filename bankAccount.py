class BankAccount:
    def __init__(self, int_rate = 0, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        elif self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5    
        return self
    def display_account_info(self):
        self.display_info = print(f"Balance: ${self.balance}") 
        return self
    def yield_interest(self):
        if self.balance >= 0:
            self.balance += (self.balance * self.int_rate)
        return self

x = BankAccount(0.05, 100)
y = BankAccount(0.02,0)

x.deposit(100).deposit(100).deposit(100).withdraw(300).yield_interest().display_account_info()
y.deposit(1100).deposit(500).withdraw(300).withdraw(300).withdraw(300).withdraw(500).yield_interest().display_account_info()