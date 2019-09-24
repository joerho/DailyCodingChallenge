class maze:
	def __init__(self, mat, start, end):
		self.dimensions = (len(mat), len(mat[0]))
		self.mat = mat
		self.visited = [[-1 if i == 1 else 0 for i in row ] for row in mat]
		self.count = [[-1 if i == 1 else 0 for i in row ] for row in mat]
		self.start = start
		self.end = end


	def has_seen(self, tup):
		return True if self.visited[tup[0]][tup[1]] else False

	def visit(self, tup):
		self.visited[tup[0]][tup[1]] = 1

	def increment(self, f, t):
		self.count[t[0]][t[1]] = self.count[f[0]][f[1]] + 1

	def dijkstra(self):
		start = self.start
		self.visit(start)
		possible = self.get_possible_moves(start)

		while len(possible) > 0:
			head = possible[0]
			possible = possible[1:]
			
			f = head[0]
			t = head[1]


			if self.has_seen(t) and self.index_count_mat(t) > self.index_count_mat(f) + 1:
				self.increment(f, t)
			else:
				self.visit(t)
				self.increment(f, t)
				possible += self.get_possible_moves(t)

			
			print(possible)


	def get_possible_moves(self, c):
		maxRow = self.dimensions[0]
		maxCol = self.dimensions[1]
		possible = list()
		#if current is in the top row
		if c[0] == 0:
			#left upper corner
			if c[1] == 0:
				possible.append((c, (0, 1)))
				possible.append((c, (1, 0)))
			#right upper corner
			elif c[1] == maxCol - 1:
				possible.append((c, (c[0], c[1] - 1)))
				possible.append((c, (c[0] + 1, c[1])))
			#general
			else:
				possible.append((c, (c[0], c[1] - 1)))
				possible.append((c, (c[0], c[1] + 1)))
				possible.append((c, (c[0] + 1, c[1])))
		#if current is in the middle rows
		elif c[0] > 0 and c[0] < maxRow - 1:
			#left side
			if c[1] == 0:
				possible.append((c, (c[0] - 1, c[1])))
				possible.append((c, (c[0] + 1, c[1])))
				possible.append((c, (c[0], c[1] + 1)))
			#right side
			elif c[1] == maxCol - 1:
				possible.append((c, (c[0] - 1, c[1])))
				possible.append((c, (c[0] + 1, c[1])))
				possible.append((c, (c[0], c[1] - 1)))
			#general
			else:
				possible.append((c, (c[0] - 1, c[1])))
				possible.append((c, (c[0] + 1, c[1])))
				possible.append((c, (c[0], c[1] - 1)))
				possible.append((c, (c[0], c[1] + 1)))

		#if current is in the bottom row
		elif c[0] == maxRow - 1:
			#left lower corner
			if c[1] == 0:
				possible.append((c, (c[0], c[1] + 1)))
				possible.append((c, (c[0] - 1, c[1])))
			#right lower corner
			elif c[1] == maxCol - 1:
				possible.append((c, (c[0], c[1] - 1)))
				possible.append((c, (c[0] - 1, c[1])))
			#general
			else:
				possible.append((c, (c[0], c[1] - 1)))
				possible.append((c, (c[0], c[1] + 1)))
				possible.append((c, (c[0] - 1, c[1])))

		#take away from possible list
		possible = [x for x in possible if (self.index(x[1]) == 0)]
		possible = [x for x in possible if (self.index_visited_mat(x[1]) == 0)]

		return possible

	def index(self, tup):
		i = tup[0]
		j = tup[1]

		return self.mat[i][j]

	def index_count_mat(self, tup):
		return self.count[tup[0]][tup[1]]

	def index_visited_mat(self,tup):
		return self.visited[tup[0]][tup[1]]


def get_min_steps(mat, start, end):

	# if index(mat, start) == 1:
	# 	return None
	# if index(mat, end) == 1:
	# 	return None

	m = maze(mat, start, end)
	m.dijkstra()

	print (m.count)
	return m.index_count_mat(end)








mat = [[0, 0, 0, 0],
	   [1, 1, 0, 1],
	   [0, 0, 0, 0],
	   [0, 0, 0, 0]]


print(get_min_steps(mat, (3,0), (0,0)))
#assert get_min_steps(mat, (3,0), (0,0)) == 7