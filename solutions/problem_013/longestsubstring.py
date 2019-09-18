
# def longestsubstring(s, k):
# 	encountered = list()
# 	max_length = 0;
# 	cur_length = 0;

# 	if len(s) == 0:
# 		return 0
# 	if len(s) == 1:
# 		return 1

# 	for char in s:
# 		if (char not in encountered and len(encountered) >= k):
# 			cur_length = k;
# 			encountered = encountered[1:]
# 			encountered.append(char)

# 		elif (char not in encountered and len(encountered) < k):
# 			encountered.append(char)
# 			cur_length += 1

# 		elif char in encountered:
# 			cur_length += 1

# 		if max_length <= cur_length:
# 			max_length = cur_length

# 		print("encountered:" + str(encountered))
# 		print("char: " + char)
# 		print("cur: " + str(cur_length))
# 		print("max: " + str(max_length))

# 	return max_length

def longestsubstring(s, k):
	


# print(longestsubstring('abcba',2))
# print(longestsubstring('abcccccccba',2))
print(longestsubstring("abcbbbabbcbbadd", 2))
# assert longestsubstring('abcba', 2) == 3
# assert longestsubstring("abcccccccba", 2) == 9
# assert longestsubstring("abcba", 2) == 3
# assert longestsubstring("abccbba", 2) == 5
# assert longestsubstring("abcbbbabbcbbadd", 2) == 6
# assert longestsubstring("abcbbbaaaaaaaaaabbcbbadd", 1) == 1
# assert longestsubstring("abccbba", 3) == 7