import json

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#wrong solution :(
def serializeWrong(root):
	if root == None:
		return "none"
	else:
		return root.val + " " +  serialize(root.left) + " " + serialize(root.right)

def deserializeWrong(serial):
	arr = serial.split(" ")
	if(arr[0]) == "none":
		return None
	else:
		return Node(arr[0], deserialize(" ".join(arr[1:])), deserialize(" ".join(arr[1:])))

#better solution
def serialize(root):
	if not root:
		return None

	serialMap = dict()
	serialLeft = serialize(root.left)
	serialRight = serialize(root.right)
	
	serialMap['val'] = root.val
	if serialLeft:
		serialMap['left'] = serialLeft
	if serialRight:
		serialMap['right'] = serialRight

	return json.dumps(serialMap)



def deserialize(serial):
	serialMap = json.loads(serial)

	node = Node(serialMap['val'])

	if 'left' in serialMap:
		node.left = deserialize(serialMap['left'])
	if 'right' in serialMap:
		node.right = deserialize(serialMap['right'])

	return node


node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(node))
assert deserialize(serialize(node)).left.left.val == 'left.left'

node_a = Node('a')
node_b = Node('b')
node_c = Node('c')
node_d = Node('d')
node_e = Node('e')
node_f = Node('f')
node_g = Node('g')
node_a.left = node_b
node_a.right = node_c
node_b.left = node_d
node_b.right = node_e
node_c.left = node_f
node_c.right = node_g

serialized_a = serialize(node_a)
deserialized_a = deserialize(serialized_a)
assert deserialized_a.val == "a"
assert deserialized_a.left.val == "b"
assert deserialized_a.left.left.val == "d"






