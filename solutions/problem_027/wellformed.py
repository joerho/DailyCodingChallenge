
brace_map = {
	")" : "(",
	"}" : "{",
	"]" : "["
}

def well_formed(string):

	stack = list()

	for char in string:
		if stack and char in brace_map and stack[-1] == brace_map[char]:
			stack.pop()
		else:
			stack.append(char)

	return not stack

assert well_formed("")
assert well_formed("{}")
assert well_formed("([])")
assert well_formed("([])[]({})")
assert not well_formed("(")
assert not well_formed("]")
assert not well_formed("((()")
assert not well_formed("([)]")