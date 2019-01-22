class Kettle(object):
	def __init__(self,make,price):
		self.make = make
		self.price = price

kenwood = Kettle('kenwood',12.75)
hamilton = Kettle('hamilton',9.99)
print('Models:{} = {}, {} = {}'.format(kenwood.make,kenwood.price,hamilton.make,hamilton.price))