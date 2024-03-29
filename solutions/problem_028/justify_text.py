

def justify_text(words, max_line_length):
	lines = list()
	current_words = list()
	line_lengths = list()
	cumulative_length = -1

	for word in words:
		if cumulative_length + (len(word) + 1) > max_line_length:
			lines.append(current_words)
			line_lengths.append(cumulative_length)
			cumulative_length = -1
			current_words = list()
		cumulative_length += (len(word) + 1)
		current_words.append(word)

	if current_words:
		lines.append(current_words)
		line_lengths.append(cumulative_length)

	justified_lines = list()
	for words, length in zip(lines, line_lengths):
		spaces_to_add = max_line_length - length
		guaranteed_spaces = 1 + (spaces_to_add // (len(words) - 1))
		bonus_space_recipients = spaces_to_add % (len(words) - 1)

		line = ""
		for (index, word) in enumerate(words[:-1]):
			line += word
			line += guaranteed_spaces * " "
			if index < bonus_space_recipients:
				line += " "

		line += words[-1]
		justified_lines.append(line)

	return justified_lines


assert justify_text(["the", "quick", "brown", "fox", "jumps",
                     "over", "the", "lazy", "dog"], 16) == \
    ['the  quick brown', 'fox  jumps  over', 'the   lazy   dog']
assert justify_text(["the", "quick", "brown", "fox", "jumps", "over"], 16) == \
    ['the  quick brown', 'fox  jumps  over']
assert justify_text(["the", "quick"], 16) == ['the        quick']


	