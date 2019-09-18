def addtotree(s, tree):
	if not s:
		return tree
	char = s[0]
	if char not in tree:
		tree[char] = dict()
	tree[char] = addtotree(s[1:], tree[char])

	return tree

def get_dict_tree(dictionary):
	tree = dict()

	for word in dictionary:
		tree = addtotree(word, tree)

	return tree

def autocomplete(s, dictionary):
	tree = get_dict_tree(dictionary)

	cur = tree
	for char in s:
		if char not in cur:
			return []
		cur = cur[char]

	completions = get_possible(cur)
	completions = [s + x for x in completions]
	return completions

def get_possible(tree):
	possible = list()
	for char in tree:
		if tree[char]:
			children = get_possible(tree[char])
			for child in children:
				possible.append(char + child)
		else:
			possible.append(char)
	return possible


assert autocomplete("de", ["dog", "deer", "deal"]) == ["deer", "deal"]
assert autocomplete("ca", ["cat", "car", "cer"]) == ["cat", "car"]
assert autocomplete("ae", ["cat", "car", "cer"]) == []
assert autocomplete("ae", []) == []

