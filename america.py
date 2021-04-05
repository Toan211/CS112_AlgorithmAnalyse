from operator import attrgetter

n = int(input())

listOfBang = []
listKetQua = []

for i in range(n):
	name, weight, value = input().split()
	listOfBang.append((name, int(value)//2+1, int(weight)))

'''
Nguồn:
https://mike.place/2017/ecknapsack/
'''

def knapsack(items, W):
	'''
	Solve knapsack problem for an iterable of items and knapsack capacity W.
	Each item is a (label, value, weight) triple.
	Returns the items selected and their total value.
	The knapsack selection is the subset of items that maximizes the total
	value of the knapsack without exceeding its capacity.
	'''
	items = list(items)
	n = len(items)
	# A[i, x] stores the solution to the optimal knapsack problem for items
	# 1..i inclusive, given a knapsack of capacity x. The items are labelled 1
	# to n, but A also stores optimal values for the empty set of items (i = 0)
	# and a zero capacity knapsack (W = 0), which are of course all zero.
	A = [[0] * (W+1) for _ in range(n+1)]

	# Populate the array A from bottom up
	for i in range(1, n+1):
		# The value and weight of the ith item in items (-1 handles Python's
		# 0-indexed arrays).
		vi = items[i-1][1]
		wi = items[i-1][2]

		for x in range(0, W+1):
			if wi <= x:
				A[i][x] = max(A[i-1][x], A[i-1][x-wi] + vi)
			else:
				A[i][x] = A[i-1][x]

	w = W
	picks = []
	for j in range(n, 0, -1):
		if (A[j][w] != A[j-1][w]):
			w -= items[j-1][2]
			picks.append(items[j-1])

	return picks, A[n][W]

def knapsackReduce(items, W):
	items = list(items)

	best_value = [0] * (W + 1)

	# Populate the array A from bottom up
	for item in items:
		for w in range(W, item[2] - 1, -1):
			value = best_value[w - item[2]] + item[1]

			if value > best_value[w]:
				best_value[w] = value


	return best_value[W]

def complementaryknapsack(items):
	'''
	Solve complementary knapsack problem for an iterable of items and knapsack
	capacity W. Each item is a (label, value, weight) triple.

	Returns the items selected and their total value.
	'''
	Wtot = sum(weight for label, value, weight in items)
	TotalPop = sum(value for label, value, weight in items)

	W = Wtot//2 + 1
	'''picks = knapsack(items, Wtot - W)
	complement = [(label, value, weight) for label, value, weight in items if label not in [labelp for labelp, _, _ in picks]]
	complementvalue = sum(value//2 + 1 for label, value, weight in complement)'''

	value = knapsackReduce(items, Wtot - W)

	return TotalPop - value



value = complementaryknapsack(listOfBang)

print(value)