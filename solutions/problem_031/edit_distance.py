

def edit_distance(s1, s2):

	len1 = len(s1)
	len2 = len(s2)

	if s1 == s2:
		return 0
	elif len1 == 0:
		return len2
	elif len2 == 0:
		return len1

	if s1[0] == s2[0]:
		return edit_distance(s1[1:], s2[1:])
	else:
		return 1 + min(
			edit_distance(s1[1:], s2),
			edit_distance(s1, s2[1:]),
			edit_distance(s1[1:], s2[1:]))


assert edit_distance("", "") == 0
assert edit_distance("a", "b") == 1
assert edit_distance("abc", "") == 3
assert edit_distance("abc", "abc") == 0
assert edit_distance("kitten", "sitting") == 3
