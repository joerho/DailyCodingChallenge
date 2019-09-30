


# def matchexp(regex, string):
# 	reglen = len(regex)
# 	strlen = len(string)

# 	if reglen > strlen:
# 		return False

# 	if '.' in regex:
# 		if reglen != strlen:
# 			return False

# 		for i in range(strlen):
# 			if regex[i] != '.':
# 				if regex[i] != string[i]:
# 					return False
# 		return True

# 	elif '*' in regex:
# 		l = strlen - reglen + 1
# 		s = string[l:]

# 		return s == regex[1:]
		
def matchexp(regex, string):
	if not regex:
		return not string

	first_char = bool(string) and (regex[0] in {string[0], '.'})

	if len(regex) >= 2 and regex[1] == '*':
		return matchexp(regex[2:], string) or (first_char and matchexp(regex, string[1:]))
	else:
		return first_char and matchexp(regex[1:], string[1:])

# assert matchexp("ra.", "ray")
# assert not matchexp("ra.", "raymond")
assert matchexp("*e", "jaljflakdsjfl;akdsnf;laksdnf;alkdsnfa;lkdnsfal;dknfe")
assert matchexp(".*at", "cxxxxxxat")
# assert not matchexp(".*at", "chats")