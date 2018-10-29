'''
create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
'''
class Account:
	# Attributes
    def __init__(self,owner,balance):
         
        self.owner = owner
        self.balance = balance
    #methods
    def deposit(self,amount):
         
        self.balance = self.balance + amount
        print("deposit accepted and {} added to your account".format(amount))


    def withdrawl(self,collection):
        if collection < self.balance:
            print("withdrawl accepted and {} deducted from your account".format(collection))
            self.balance = self.balance - collection
        else:
        	print("withdrawl Denied")




account1 = Account('Amreesh',500.0)
account1.owner
account1.deposit(100)
account1.balance
account1.withdrawl(200)
account1.withdrawl(800)
