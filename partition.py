j = int(input())
partitions = {}
def memoiz(part,partition):
    partitions[partition] = part
def p(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if n in partitions:
        return partitions[n]
    sign = 1
    Psum = 0
    for k in range(1,int(n+1)):
        p1 = n - k*(3*k - 1)/2
        p2 = n - k*(3*k + 1)/2
        if (p1 < 0 and p2 < 0):
            break
        if p1 >= 0:
            part1 = p(p1)
            memoiz(part1,p1)
        else:
            part1 = 0
        if p2 >= 0:
            part2 = p(p2)
            memoiz(part2,p2)
        else:
            part2 = 0
        parts = part1 + part2
        Psum = Psum + sign*parts
        sign = -sign
    return Psum%(10**17+3)
for i in range(0,j,100):
    p(i)
h = p(j)
print(h)