m, n = input().split()

m = int(m)
n = int(n)

banDo = []
memoi = {}

for i in range(m):
	temp = input().split()
	tempList = []

	for element in temp:
		tempList.append(int(element))

	banDo.append(tempList)

def F(x, y):
	if x == 0 and y == 0:
		return 1
	if x < 0 or y < 0:
		return 0
	if banDo[x][y] == 0:
		return 0

	coordinate = (x, y)

	if coordinate in memoi.keys():
		return memoi[coordinate]

	memoi[coordinate] = F(x-1, y) + F(x, y-1)
	print(memoi[coordinate])

	return memoi[coordinate]

def FBottom(x, y):
	memoi = [[0 for j in range(n)] for i in range(m)]
	memoi[0][0] = 1

	up = 0
	left = 0

	for i in range(m):
		for j in range(1, n):
			if j-1 < 0:
				left = 0
			elif banDo[i][j-1] == 0:
				left = 0
			else:
				left = memoi[i][j-1]

			if i-1 < 0:
				up = 0
			elif banDo[i-1][j] == 0:
				up = 0
			else:
				up = memoi[i-1][j]

			memoi[i][j] = up + left

	return memoi[x][y]


def uniquePathsWithObstacles(A):
	num_rows = len(A)
	num_columns = len(A[0])

	prev_row = [0] * num_columns
	prev_row[0] = A[0][0]

	for r in range(num_rows):
		if r == 0:
			current_row = [A[r][0] and prev_row[0]]
		elif prev_row[0] != 0 and A[r][0] != 0:
			current_row = [A[r][0] + prev_row[0]]
		else:
			current_row = [0]

		for c in range(1, num_columns):
			if A[r][c] == 0:
				paths = 0
			else:
				paths = A[r][c] + max(current_row[-1], prev_row[c])
			current_row.append(paths)

		prev_row = current_row

	return prev_row[-1]

banDo2 = [[1]*n for _ in range(m)]

for row in range(m):
	for col in range(n):
		if banDo[row][col] == 0:
			banDo2[row][col] = 0

soCachDi = uniquePathsWithObstacles(banDo)
print(soCachDi)