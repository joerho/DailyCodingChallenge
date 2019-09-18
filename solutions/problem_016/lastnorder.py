class Log:
	def __init__(self, size):
		self._size = size
		self._arr = None
		self._count = 0

	def record(self, order_id):
		# arr = self._arr
		if not self._arr:
			self._arr = list()
			self._arr.append(order_id) 
		elif len(self._arr) < self._size:
			self._arr.append(order_id)
		elif len(self._arr) == self._size:
			self._arr = self._arr[1:]
			self._arr.append(order_id)


	def get_last(self, i):
		if not self._arr:
			return None
		else:
			return self._arr[i]




log = Log(5)
for i in range(7):
	log.record(i)


# print(log.get_last(0))
# print(log.get_last(1))
assert log.get_last(0) == 2

# [0,1,2,3,4,5,6]

# arr = list()
# for i in range(7):
# 	arr.append(i)

# print(arr)
# print(arr[1:].append(7))
# q = arr[1:].append(7)
# p = (arr[1:]).append(7)
# g = arr[1:]
# g.append(7)
# print(q)
# print(p)
# print(g)





