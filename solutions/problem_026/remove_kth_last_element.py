



class LinkedList:
	class Node:
		def __init__(self, val, next_node = None):
			self.val = val
			self.index = 0
			self.next_node = next_node

	def __init__(self):
		self.start = None
		self.last = None
		self.size = 0

	def __repr__(self):
		cur = self.start
		output = "{}".format(cur.val)
		cur = cur.next_node
		while cur:
			output += " -> {}".format(cur.val)
			cur = cur.next_node

		return output

	def add(self, val):
		temp = self.Node(val)
		if not self.start:
			self.start = temp
			self.last = temp
		else:
			temp.index += self.last.index
			prev = self.last
			self.last = temp
			prev.next_node = temp
			

		self.size += 1

		return temp

	def remove(self, k):
		index = self.size - k
		temp = self.start

		while index > 0:
			prev = temp
			temp = temp.next_node
			index-=1

		prev.next_node = temp.next_node
		self.size-=1	

l = LinkedList()
l.add(0)
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)
l.add(6)
l.remove(2)
print(l)







