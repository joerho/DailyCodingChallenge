def getPositives(arr):
	i = 0
	j = len(arr) - 1

	while (i < j):
		if arr[i] > 0 and arr[j] <= 0:
			arr[i], arr[j] = arr[j], arr[i]
		elif arr[i] > 0:
			j -= 1
		else:
			i += 1

	pivot = i if arr[i] > 0 else i + 1
	return arr[pivot:] 


def getMissing(arr):
	if not arr:
		return 1

	pos = getPositives(arr)
	size = len(pos)

	if not pos:
		return 1

	for num in pos:
		cur = abs(num)
		if ((cur - 1) < size) and (pos[cur - 1] > 0):
			pos[cur - 1] *= -1

	for i,num in enumerate(pos):
		if num > 0:
			return (i + 1)

	return(size + 1)


# print(getMissing2([1,1,3]))
# print(getMissing2([1,1,1,1,5]))
# print(getMissing2([1,2,0]))
# print(getMissing2([3,4,6,5,1,10]))
print(getPositives([3,4,-1,1]))
print(getPositives([-1,-1,-1,-2,-2]))
assert getMissing([3, 4, -1, 1]) == 2
assert getMissing([1, 2, 0]) == 3
assert getMissing([1, 2, 5]) == 3
assert getMissing([1]) == 2
assert getMissing([-1, -2]) == 1
assert getMissing([]) == 1
assert getMissing([1,1,3]) == 2