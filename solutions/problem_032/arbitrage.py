from math import log

def arbitrage(table):
	transformed_graph = [[-log(edge) for edge in row] for row in table]

	source = 0
	n = len(transformed_graph)
	min_dist = [float('inf')] * n

	min_dist[source] = 0

	for i in range(n - 1):
		for v in range(n):
			for w in range(n):
				if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
					mindist[w] = min_dist[v] + transformed_graph[v][w]

	for v in range(n):
		for w in range(n):
			if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
				return True

	return False