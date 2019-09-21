class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

	def __repr__(self):
		output = list()
		output.append(self.val)
		temp = self.next
		while temp:
			output.append(temp.val)
			temp = temp.next

		return str(output)

	def add(self, temp):
		self.next = temp

def intersecting_node(a, b):
	def get_length(head):
		length = 0
		temp = head
		while temp:
			length += 1
			temp = temp.next

		return length
	
	len_a = get_length(a)
	len_b = get_length(b)
	min_len = min(len_a, len_b)

	for _ in range(len_a - min_len):
		a = a.next

	for _ in range(len_b - min_len):
		b = b.next

	for _ in range(min_len):
		if a.val == b.val:
			return a

		a = a.next
		b = b.next


# a = 3 7 8 10
# b = 99 1 8 10
a = Node(3)
b = Node(7)
c = Node(8)
d = Node(10)
e = Node(99)
f = Node(1)

a.add(b)
b.add(c)
c.add(d)

e.add(f)
f.add(c)

print (intersecting_node(a, e))
