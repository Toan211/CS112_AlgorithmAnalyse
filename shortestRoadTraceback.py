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

def uniquePathsWithObstacles(A):
	num_rows = len(A)
	num_columns = len(A[0])

	prev_row = [(0, [])] * num_columns
	prev_row[0] = (A[0][0], [(0, 0)] + prev_row[0][1])

	for r in range(num_rows):
		if r == 0:
			current_row = [(A[r][0] and prev_row[0][0], prev_row[0][1])]
		elif prev_row[0] != 0 and A[r][0] != 0:
			current_row = [(A[r][0] + prev_row[0][0], [(r, 0)] + prev_row[0][1])]
		else:
			current_row = [(0, [])]

		for c in range(1, num_columns):
			if A[r][c] == 0:
				current_row.append((0, []))
			else:
				if current_row[-1][0] > prev_row[c][0]:
					paths = A[r][c] + current_row[-1][0]
					current_row.append((paths, [(r, c)] + current_row[-1][1]))
				else:
					paths = A[r][c] + prev_row[c][0]
					current_row.append((paths, [(r, c)] + prev_row[c][1]))


		prev_row = current_row

	return prev_row[-1]


ketQua = uniquePathsWithObstacles(banDo)
value = ketQua[0]
duongDi = ketQua[1]

print(value)
for path in duongDi:
	print(str(path[0]) + ' ' + str(path[1]))