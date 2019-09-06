import sys

def checkSum(arr, answer):
	for i in arr:
		for j in arr:
			if i + j == answer:
				return True
	return False

def checkSumSet(arr, answer):
	possibleAnswers = set()
	for i in arr:
		if i in possibleAnswers:
			return True
		possibleAnswers.add(answer - i)
	return False

assert not checkSumSet([], 17)
assert checkSumSet([10, 15, 3, 7], 17)
assert not checkSumSet([10, 15, 3, 4], 17)