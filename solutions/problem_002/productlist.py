#O(n^2)
def productOfList(arr):
	newArr = []
	for i in range(len(arr)):
		temp = 1
		for j in range(len(arr)):
			if (i != j):
				temp *= arr[j]
		newArr.append(temp)
	return newArr

#O(n)
def productOfList2(arr):
	cumulative = 1
	rightProd = list()
	for num in arr:
		cumulative *= num
		rightProd.append(cumulative)

	cumulative = 1
	leftProd = list()
	for num in arr[::-1]:
		cumulative *= num
		leftProd.append(cumulative)
	leftProd = leftProd[::-1]

	output = list()
	for i in range(len(arr)):
		if i == 0:
			output.append(leftProd[i + 1])
		elif i == len(arr) - 1:
			output.append(rightProd[i - 1])
		else:
			output.append(leftProd[i + 1] * rightProd[i - 1])
	return output


productOfList2([1,2,3,4,5])



assert (productOfList([1,2,3,4,5]) == [120,60,40,30,24])
assert (productOfList([3,2,1]) == [2,3,6])

assert (productOfList2([1,2,3,4,5]) == [120,60,40,30,24])
assert (productOfList2([3,2,1]) == [2,3,6])


