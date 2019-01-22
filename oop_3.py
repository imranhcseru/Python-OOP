class Kettle(object):
	power_source = 'electricity'
	def __init__(self,make,price):
		self.make = make
		self.price = price
		self.on = False

	def switched_on(self):
		self.on = True


kenwood = Kettle('kenwood',12.85)
hamilton = Kettle('hamilton',9.75)
kenwood.switched_on()
kenwood.power_source = 'Gas'
print('Model: {0.make} = {0.price} {0.on} {0.power_source}, {1.make} = {1.price} {1.on} {1.power_source}'.format(kenwood,hamilton))