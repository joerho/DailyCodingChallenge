


def encode(s):
	char_list = list()
	prev_char = None
	char_count = 0

	for char in s:
		if prev_char == char or not prev_char:
			char_count += 1
		else:
			char_list.append(str(char_count))
			char_list.append(prev_char)
			char_count = 1

		prev_char = char

	if char_count > 0:
		char_list.append(str(char_count))
		char_list.append(prev_char)

	return "".join(char_list)


def decode(s):
	char_list = list()
	index = 0

	while index < len(s):
		char_list.append(int(s[index]) * s[index + 1])
		index += 2
	return "".join(char_list)


assert encode("AAAABBBCCDAA") == "4A3B2C1D2A"
assert decode("4A3B2C1D2A") == "AAAABBBCCDAA"
