class Account:
	def __init__(self,name,balance):
		self.name = name
		self.balance = balance
		print("Account Holder: {} . Initial balance: {}".format(self.name,self.balance))

	def deposite(self,amount):
		self.balance = self.balance + amount
		print('balance after deposite:')
		self.show_balance()

	def withdraw(self,amount):
		self.balance = self.balance - amount
		self.show_balance()

	def show_balance(self):
		print(self.balance)

if __name__ == '__main__':
	tim = Account('Tim',2000)
	tim.deposite(2000)
	tim.withdraw(500)