import math
from collections import deque

class Graph(object):
	def __init__(self, adjacency_list=dict(), edge_weights=dict()):
		self.__adjacency_list = adjacency_list.copy()
		self.__edge_weights = edge_weights.copy()

	def add_edge(self, u, v, w):
		""" Add a new edge u -> v to graph with edge weight w. """
		self.__edge_weights[u, v] = w
		if u not in self.__adjacency_list:
			self.__adjacency_list[u] = set()
		self.__adjacency_list[u].add(v)

	def get_edge_weight(self, u, v):
		""" Get edge weight of edge between u and v. """
		return self.__edge_weights[u, v]

	def get_adjacent_nodes(self, u):
		""" Get nodes adjacent to u. """
		return self.__adjacency_list.get(u, set())

	def get_number_of_nodes(self):
		""" Return the total number of nodes in graph. """
		return len(self.__adjacency_list)

	def get_nodes(self):
		""" Return all nodes in this graph. """
		return self.__adjacency_list.keys()

	def Print(self):
		for u in self.get_nodes():
			adj = self.get_adjacent_nodes(u)
			for v in adj:
				print("Node %s: connected to %s node" % (u, v))

class AbstractDijkstraSPF(object):
	""" Dijkstra's shortest path algorithm, abstract class. """

	def __init__(self, G, s):
		""" Calculate shortest path from s to other nodes in G. """
		self.__dist = dist = dict()
		self.__prev = prev = dict()
		visited = set()
		queue = set()

		dist[s] = 0
		prev[s] = s
		queue.add(s)

		while queue:
			u = min(queue, key=dist.get)
			for v in self.get_adjacent_nodes(G, u):
				if v in visited:
					continue
				alt = self.get_distance(u) + self.get_edge_weight(G, u, v)
				if alt < self.get_distance(v):
					dist[v] = alt
					prev[v] = u
					queue.add(v)
			queue.remove(u)
			visited.add(u)

	@staticmethod
	def get_adjacent_nodes(G, u):
		raise NotImplementedError()

	@staticmethod
	def get_edge_weight(G, u, v):
		raise NotImplementedError()

	def get_distance(self, u):
		""" Return the length of shortest path from s to u. """
		return self.__dist.get(u, math.inf)

	def get_path(self, v):
		""" Return the shortest path to v. """
		path = [v]
		while self.__prev[v] != v:
			v = self.__prev[v]
			path.append(v)
		return path[::-1]




class DijkstraSPF(AbstractDijkstraSPF):

	@staticmethod
	def get_adjacent_nodes(G, u):
		return G.get_adjacent_nodes(u)

	@staticmethod
	def get_edge_weight(G, u, v):
		return G.get_edge_weight(u, v)


class State:
	def __init__(self, listState, cost, visited):
		self.listState = listState
		self.cost = cost
		self.visited = visited

	def Print(self):
		print(*self.listState, end=' ')

n, begin = input().split()
n = int(n)

graph = Graph()

for i in range(n):
	u, v, w = input().split()
	w = int(w)
	graph.add_edge(u, v, w)

startList = [begin]
startState = State(startList, 0, {})

def BFS(graph, startState):
	numberOfNode = graph.get_number_of_nodes()

	bestState = None
	minWeight = 999999

	frontier = deque()
	frontier.append(startState)

	value = tuple(startState.listState)
	explored = {}
	explored[value] = True

	while frontier:
		state = frontier.pop()

		if len(state.listState) == numberOfNode + 1:
			if state.cost < minWeight:
				bestState = state
				minWeight = state.cost
		elif len(state.listState) > numberOfNode + 1:
			break

		for node in graph.get_adjacent_nodes(state.listState[-1]):
			if node != begin:
				if node != state.listState[-1] and node not in state.visited.keys():
					state.listState.append(node)
					value = tuple(state.listState)

					if value not in explored.keys():
						newState = state.listState[:]
						weight = graph.get_edge_weight(state.listState[-2], node)
						visitedNew = state.visited.copy()
						visitedNew[node] = True
						frontier.append(State(newState, state.cost + weight, visitedNew))
						explored[value] = True

					del state.listState[-1]

			else:
				if len(state.listState) == numberOfNode:
					state.listState.append(node)
					value = tuple(state.listState)

					if value not in explored.keys():
						newState = state.listState[:]
						weight = graph.get_edge_weight(state.listState[-2], node)
						visitedNew = state.visited.copy()
						visitedNew[node] = True
						frontier.append(State(newState, state.cost + weight, visitedNew))
						explored[value] = True

					del state.listState[-1]


	return bestState

result = BFS(graph, startState)

result.Print()