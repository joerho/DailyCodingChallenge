from collections import deque

def sliding_max(arr, k):
	window_max = list()

	if not arr:
		return None
	if k > len(arr):
		return max(arr)

	dq = deque()

	for i in range(k):
		while dq and arr[dq[-1]] < arr[i]:
			dq.pop()
		dq.append(i)
	window_max.append(arr[dq[0]])

	for i in range(k, len(arr)):
		while dq and dq[0] <= i - k:
			dq.popleft()

		while dq and arr[dq[-1]] < arr[i]:
			dq.pop()
		dq.append(i)

		window_max.append(arr[dq[0]])

	return window_max

assert sliding_max([10, 5, 2, 7, 8, 7], 3) == [10, 7, 8, 8]
assert sliding_max([5, 2, 1], 2) == [5, 2]