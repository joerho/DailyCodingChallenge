import heapq

def min_number_rooms(arr):
	heapq.heapify(arr)
	if not arr:
		return 0
	if len(arr) == 1:
		return 1

	rooms = 1
	head = arr[0]
	tail = arr[1:]
	end = head[1]

	while tail:
		if end > tail[0][0]:
			rooms += 1
		if end <= tail[0][0]:
			end = tail[0][1]

		head = tail[0]
		tail = tail[1:]

	return rooms

assert min_number_rooms([(30,75), (0,50), (60, 150)]) == 2
assert min_number_rooms([(0, 10), (5, 20), (10, 30), (15,25)]) == 3
assert min_number_rooms([]) == 0
assert min_number_rooms([(30, 75), (0, 50), (60, 150)]) == 2
assert min_number_rooms([(30, 75), (0, 50), (10, 60), (60, 150)]) == 3
assert min_number_rooms([(60, 150)]) == 1
assert min_number_rooms([(60, 150), (150, 170)]) == 1
assert min_number_rooms([(60, 150), (60, 150), (150, 170)]) == 2