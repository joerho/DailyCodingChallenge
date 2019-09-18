

def get_step_combos(n, x):
	combos = list()

	if (n < min(x)):
		return combos

	for size in x:
		if size == n:
			combos.append([size])
		elif n > size:
			child_combos = get_step_combos(n - size, x)
			for child in child_combos:
				combos.append([size] + child)

	return combos 

assert get_step_combos(4, [1, 2]) == \
    [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]]
assert get_step_combos(4, [1, 2, 3]) == \
    [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [1, 3], [2, 1, 1], [2, 2], [3, 1]]