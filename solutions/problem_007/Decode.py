def is_char(subcode):
	return 0 if subcode > 26 or subcode < 1 else 1

def decode(code):
	code_str = str(code)
	if len(code_str) == 1:
		count = 1

	elif len(code_str) == 2:
		count = 1 + is_char(code)

	else:
		count = decode(int(code_str[1:]))
		if is_char(int(code_str[:2])):
			count += decode(int(code_str[2:]))

	return count


assert decode(81) == 1
assert decode(11) == 2
assert decode(111) == 3
assert decode(1111) == 5
assert decode(1311) == 4


