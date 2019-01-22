class Kettle(object):

	def __init__(self,make,price):
		self.make = make
		self.price = price
		self.on = False

	def switch_on(self):
		self.on = True


kenwood = Kettle('kenwood',9.75)
hamilton = Kettle('hamilton',12.25)

print('Models: {0.make} = {0.price} and {0.on}, {1.make} = {1.price} and {0.on}'.format(kenwood,hamilton))
kenwood.switch_on()
print('Models: {0.make} = {0.price} and {0.on}, {1.make} = {1.price} and {0.on}'.format(kenwood,hamilton))
