
class Node:
	def __init__(self, val, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

def countUnival(root):
	if (root == None):
		return 0
	if (root.left == None and root.right == None):
		return 1
	elif (root.left == None and root.right != None):
		return countUnival(root.right)
	elif (root.left != None and root.right == None):
		return countUnival(root.left)
	elif (root.val == root.left.val == root.right.val):
		return 1 + countUnival(root.left) + countUnival(root.right)
	else:
		return countUnival(root.left) + countUnival(root.right)



root = Node(0)
node1 = Node(1)
node2 = Node(0)
node3 = Node(1)
node4 = Node(0)
node5 = Node(1)
node6 = Node(1)
root.left = node1
root.right = node2
node2.left = node3
node2.right = node4
node3.left = node5
node3.right = node6


assert countUnival(None) == 0
assert countUnival(root) == 5
assert countUnival(node2) == 4
assert countUnival(node6) == 1
assert countUnival(node3) == 3

