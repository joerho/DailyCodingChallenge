


def water_trap(walls):

	if len(walls) < 3:
		return 0

	total_volume = 0

	left = 0
	right = len(walls) - 1
	left_max = 0
	right_max = 0

	while left <= right:
		if walls[left] < walls[right]:
			if walls[left] > left_max:
				left_max = walls[left]
			else:
				total_volume += left_max - walls[left]

			left += 1

		else:
			if walls[right] > right_max:
				right_max = walls[right]
			else:
				total_volume += right_max - walls[right]

			right -= 1

	return total_volume


assert water_trap([1]) == 0
assert water_trap([2, 1]) == 0
assert water_trap([2, 1, 2]) == 1
assert water_trap([4, 1, 2]) == 1
assert water_trap([4, 1, 2, 3]) == 3
assert water_trap([3, 0, 1, 3, 0, 5]) == 8
assert water_trap([10, 9, 1, 1, 6]) == 10