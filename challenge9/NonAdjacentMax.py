def getNonAdjacentMaX(array):
	previous, largest = 0, 0
	for amount in array:
		previous, largest = largest, max(largest, previous + amount)
	return largest

# print(getNonAdjacentMaX([2, 4, 6, 8]))
# print(getNonAdjacentMaX([5, 1, 1, 5]))

assert getNonAdjacentMaX([2,4,6,8]) == 12
assert getNonAdjacentMaX([5,1,1,5]) == 10
