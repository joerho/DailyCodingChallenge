
#o(nlogn)? 
def missingPositiveInteger(arr):
	arr.sort()

	positiveSet = set()
	[positiveSet.add(x) for x in arr if x > 0]


	least = min(positiveSet)
	most = max(positiveSet)

	for x in range(least, most+2):
		if not x in positiveSet:
			return x

	return x

def getPositive(arr):
	i = 0
	j = len(arr) - 1

	while (i < j):
		if arr[i] > 0 and arr[j] <= 0:
			arr[i], arr[j] = arr[j], arr[i]
		elif arr[i] > 0:
			j -= 1
		else:
			i += 1

	#need this because of the case when every number is negative
	pivot = i if arr[i] > 0 else i + 1
	return arr[pivot:]

def getMissing(arr):
	if not arr:
		return(1)

	positives = getPositive(arr)
	length = len(positives)

	if not positives:
		return(1)

	# if max(positives) == length:
	# 	return max(positives) + 1

	for num in positives:
		cur = abs(num)
		if ((cur - 1) < length) and positives[cur-1] > 0:
			positives[cur - 1] *= -1

	#go through each element and find the first one that was not visited
	for i, num in enumerate(positives):
		if num > 0:
			return i + 1

	#every element is negative (all were visited)
	return (length + 1)



# print(getMissing([1,1,3]))
# print(getMissing([1,1,1,1,5]))
# print(getMissing([1,2,0]))
# print(getMissing([3,4,6,5,1,10]))
print(getPositive([3,4,-1,1]))
print(getPositive([-1,-1,-1,-2,-2]))
assert getMissing([3, 4, -1, 1]) == 2
assert getMissing([1, 2, 0]) == 3
assert getMissing([1, 2, 5]) == 3
assert getMissing([1]) == 2
assert getMissing([-1, -2]) == 1
assert getMissing([]) == 1
assert getMissing([1,1,3]) == 2




