'''Bank Account Manager
Under the Classes section in the list of suggested final capstone projects is a Bank Account Manager program. 
The goal is to create a class called Account which will be an abstract class for three other classes called CheckingAccount, SavingsAccount
and BusinessAccount. Then you should manage credits and debits from these accounts through an ATM style program.

Project Scope
To tackle this project, first consider what has to happen.

There will be three different types of bank account (Checking, Savings, Business)
Each account will accept deposits and withdrawals, and will need to report balances
Project Wishlist:-
We might consider additional features, like:

impose a monthly maintenance fee
waive fees for minimum combined deposit balances
each account may have additional properties unique to that account:
Checking allows unlimited transactions, and may keep track of printed checks
Savings limits the number of withdrawals per period, and may earn interest
Business may impose transaction fees
automatically transfer the "change" for debit card purchases from Checking to Savings, 
where "change" is the amount needed to raise a debit to the nearest whole dollar
permit savings autodraft overdraft protection'''

# creating an class Account with attributes account holder name and opening balance
class Account:
	def __init__(self,account_num,opening_bal):
	    self.account_num = account_num
	    self.balance = opening_bal
	# defining a string method for rupees to be stick to any amount
	def __str__(self):
	    return f'${self.balance:.2f}'
	# defining two methods for deposit and withdrawl
	def deposit(self,dep_amount):
	    self.balance += dep_amount
	def withdrawals(self,wid_amount):
	    if wid_amount > self.balance:
	       print('transaction denied')
	    else:
	       self.balance -=wid_amount

# making checking Account as abstract class
class Checking(Account):
	def __init__(self,account_num,opening_bal):
	#run base class
	    super().__init__(account_num,opening_bal)
	def __str__(self):
	    return f'CheckingAccount#{self.account_num}\n Balance:{Account.__str__(self)}'
class Business(Account):
	def __init__(self,account_num,opening_bal):
	#run base class
	    super().__init__(account_num,opening_bal)
	def __str__(self):
	    return f'Business Account#{self.account_num}\n Balance:{Account.__str__(self)}'
class Savings(Account):
	def __init__(self,account_num,opening_bal):
	#run base class
	    super().__init__(account_num,opening_bal)
	def __str__(self):
	    return f'Savings Account#{self.account_num}\n Balance:{Account.__str__(self)}
class Customer:
      def __init__(self,name,PIN):
          self.name = name
          self.PIN = PIN
# create a dictionary of accounts with lists to hold multiple accounts
          self.accts = {'c':[],'s':[],'B':[]}
      def __str__(self):
          return self.name
      def open_checking(self,account_num,opening_bal):
          self.accts['c'].append(Checking(account_num,opening_bal))
      def open_savings(self,account_num,opening_bal):
          self.accts['c'].append(Savings(account_num,opening_bal))
      def open_Business(self,account_num,opening_bal):
          self.accts['c'].append(Business(account_num,opening_bal))
    # to get total deposit
      def get_total_deposit(self):
          total = 0
          for acct in self.accts['c']:
              print(acct)
              total += acct.balance
          for acct in self.accts['s']:
              print(acct)
              total += acct.balance
          for acct in self.accts['B']:
              print(acct)
              total += acct.balance
          print(f'combined deposits:${total:.2f}')
def make_dep(cust,acct_type,acct_nbr,dep_amt):
    '''
    cust = variable name
    acct type = string 'C' 's' or 'B'
    acct_num = acct_nbr
    dep_amt = deposited amount
    '''
    for acct in cust.accts[acct_type]:
        if acct.account_num == acct_nbr:
            acct.deposit(dep_amt)
def make_wd(cust,acct_type,acct_nbr,wd_amt):
    '''
    cust = variable name
    acct type = string 'C' 's' or 'B'
    acct_num = acct_nbr
    dep_amt = deposited amount
    '''
    for acct in cust.accts[acct_type]:
        if acct.account_num == acct_nbr:
            acct.withdraw(wd_amt)
