class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if(amount<10000000):
            self.balance += amount
            print(f"Deposit of {amount} accepted. Balance: {self.balance}")
        else: 
            print("Where did you get this?")

        

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} accepted. Balance: {self.balance}")
        else:
            print("Insufficient")

account = Account("Linus", 100000)
account.deposit(10000000)

