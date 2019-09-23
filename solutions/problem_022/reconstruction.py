

def reconstruction(s, dictionary):

	if not dictionary or not s:
		return []

	dictionary_set = set(dictionary)
	arr = list()

	for i in range(len(s)):
		if s[0:i + 1] in dictionary_set:
			arr.append(s[0:i + 1])
			dictionary_set.remove(s[0:i + 1])
			arr += reconstruction(s[i+1:], dictionary_set)
			break

	return arr


assert reconstruction("thequickbrownfox", ['quick', 'brown', 'the', 'fox']) == [
    'the', 'quick', 'brown', 'fox']
assert reconstruction("bedbathandbeyond", [
                          'bed', 'bath', 'bedbath', 'and', 'beyond']) == ['bed', 'bath', 'and', 'beyond']
