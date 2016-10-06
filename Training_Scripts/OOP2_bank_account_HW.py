""" class Account() is a class that simulates simple bank account behaviour.
The object of that class is able to (has the following methods)
.balance - keep bank account balance; @property allows to use thos method without parenthesis
.deposit() - perform adding money to deposit
.limit() - define credit limit and charge
.withdaw() - take mony from account
.transfer() - move money from one account  to another
Child class PaymentAccount - allows all the same, but not deposit is allowed.

Not fault tolerant.
"""

class Account():
	def __init__(self, initial_balance=0):
		self._balance = initial_balance	
		self.lim = 0
		self.charge = 0

	@property
	def balance(self):
		return self._balance

	def deposit(self, sum=0):
		self._balance += sum
		print('You have an income {}'.format(sum), '\nYour current balance is:', self._balance)

	def limit(self, lim, charge):
		self.lim = lim -lim*charge/100
		self.charge = charge

	def withdraw(self, sum):
		if (self._balance - sum) >= 0:
			self._balance -= sum
			print('You have withdrawal {}'.format(sum), '\nYour current balance is:', self._balance)
		elif (self.lim == 0) or ((sum > self._balance) and ((self._balance - sum) > self.lim)):
			print('Not enough money')
		else:
			self._balance -= sum
			self.credit = -self._balance
			self.charged = self.credit*self.charge/100
			self._balance -= self.charged
			print('You have withdrawal {}'.format(sum), '\nYour charge for the credit is:', self.charged, '\nYour current balance is:', self._balance)

	def transfer(self, receiver, sum):
		if (self._balance - sum) >= 0:
			self._balance -= sum
			receiver._balance += sum
			print('You have transferred {}'.format(sum),'\nYour current balance is:', self._balance)
		elif (self.lim == 0) or ((sum > self._balance) and ((self._balance - sum) > self.lim)):
			print('Not enough money')
		# elif (sum > self._balance) and ((self._balance - sum) <= self.limit):
		else:
			self._balance -= sum
			self.credit = -self._balance
			self.charged = self.credit*self.charge/100
			self._balance -= self.charged
			receiver._balance += sum
			print('You have transferred {}'.format(sum), '\nYour charge for the credit is:', self.charged,'\nYour current balance is:', self._balance)


class PaymentAccount(Account):
	def deposit(self):
		print('Deposit is not allowed for the Payment Account')

# Simple checks
# MyAccount = Account(100)
# MyAccount.balance = 100
# MyAccount.sum = 15
# MyAccount.deposit(15)
# MyAccount.limit(20, 3)
# MyAccount.withdraw(75)
# MyAccount.withdraw(26)

#Transfer checks
# ac1 = Account (10)
# ac2 = Account (5)
# ac1.limit(20, 5)
# print (ac1.transfer(ac2, 30))
# print (ac2.balance)

# @property check
# a = Account(10)
# print (a.balance) # returns function like simple attribute, better data abstraction
