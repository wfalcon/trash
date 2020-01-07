class CountFromBy:
	def __init__(self, v: int = 0, i:int = 1) -> None:
		self.val = v
		self.incr = i

	def __repr__(self) -> str:
		return str(self.val)

	def increase(self) -> None:
		self.val += self.incr



q=CountFromBy(100,10)
print('q =', q.val)
q.increase()
print('q.1=', q.val)
print('-'*10)

h=CountFromBy(10,2)
print('h =', h.val)
h.increase()
print('h.1=', h.val)
print('-'*10)