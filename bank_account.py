# Create a class called BankAccount.
class BankAccount:

# Add a class variable called interest_rate that is a float representing the interest rate for
# all the accounts in the bank. This is a class variable because it is the same value for all accounts.
    interest_rate = 1.25

# Add another class variable called accounts that starts as an empty list.
# This will eventually store the collection of all bank accounts in the bank.

    accounts = []

# Add an __init__() instance method that sets the bank account's balance to zero.
# Balance is stored in an instance variable because the value needs to be different from account to account.

    def __init__(self, balance = 0):
        self.balance = balance

# Add an instance method called deposit that accepts a number as an argument and
# adds that amount to the account's balance.
# This needs to be an instance method because it pertains to a single, specific account.

    def deposit(self, amount):
        self.balance += amount
        return self.balance

# Add an instance method called withdraw that accepts a number as an argument and subtracts that
# amount from the account's balance.

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

# Add a class method called create that makes a new instance using BankAccount()
# and adds the new object to the accounts class variable so that we can find it again in the future.
# This method should return the new account object.
# This needs to be a class method because at the time we run it there is no single,
# specific account object that we are working on.

    @classmethod
    def create(cls):
        new_account = BankAccount()
        cls.accounts.append(new_account)
        return new_account

# Add a class method called total_funds that returns the sum of all balances across all
# accounts in the accounts class variable.
# This needs to be a class method because it does not pertain to any single, specific account.

    @classmethod
    def total_funds(cls):
        total_balance = 0
        for account in cls.accounts:
            total_balance += account.balance
        return total_balance

# Add a class method called interest_time that iterates through all accounts and increases their
# balances according to the class interest_rate. This needs to be a class method because it operates
# on all bank accounts, not a single, specific account.

    @classmethod
    def interest_time(cls):
        for account in cls.accounts:
            account.balance *= cls.interest_rate
        return account.balance


my_account = BankAccount.create()
your_account = BankAccount.create()
print(my_account.balance)
print(your_account.balance)
my_account.deposit(200)
your_account.deposit(1000)

print(my_account.balance) # 200.0
print(your_account.balance) # 1000.0
print(BankAccount.total_funds()) # 1200.0

BankAccount.interest_time()
print(my_account.balance) # 250.0
print(your_account.balance) # 1250.0
print(BankAccount.total_funds()) # 1500.0

my_account.withdraw(50)
print(my_account.balance) # 200.0

print(BankAccount.total_funds()) # 1450.0
