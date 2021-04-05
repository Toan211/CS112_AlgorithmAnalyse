a , b = input().split()
a = int(a)
b = int(b)
matrix = [list(map(int, input().split())) for i in range(a)]

def shortest(a,b,memoi):
    if a == 0 and b == 0:
        memoi[a][b] = 1
        return 1
    if a < 0 or b < 0:
        return 0
    if matrix[a][b] == 0:
        memoi[a][b] = 0
        return 0    
    elif memoi[a][b] != -1:
        return memoi[a][b]
    memoi[a][b] = (shortest(a - 1,b,memoi) + shortest(a,b-1,memoi))%(10**13+1)
    return memoi[a][b]
memoii = [[-1 for j in range(b)] for i in range(a)]
for i in range(0, a, 100):
    for j in range(0, b, 100):
        shortest(i, j, memoii)
h = shortest(a-1,b-1,memoii)
print(h)