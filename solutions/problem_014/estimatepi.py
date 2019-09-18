from random import random
radius = 2

def estimate_pi(iterations):
	pi_counter = 0
	rsquared = radius ** 2
	for _ in range(iterations):
		y_rand = random() * radius
		x_rand = random() * radius
		if (x_rand ** 2) + (y_rand ** 2) < rsquared:
			pi_counter += 1

	return 4 * pi_counter / iterations

assert round(estimate_pi(100000000), 3) == 3.141