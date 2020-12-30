C = [2,5,10,20,50]

def F(X, memoi = {}):
    if X<2: return 0
    if X in C: return 1
    if X in memoi[X]:return memoi[X]
    B = [F(X-x) for x in C]
    B = [i for i in B if i> 0]

    if B == []: return 0
    memoi[X] = 1+ min(B)
    return memoi[X]

def FBottom(X):
    memoi = (X+51)*[0]
    for i in range(2, X+1):
        if i in C: memoi[i] = 1
        else:
            B = [memoi[i-x] for x in C]
            B = [j for j in B if j>0]
            if B == []: memoi[i] = 0
            else: memoi[i] = 1 +min(B)
        pass
    return memoi[X]

print(FBottom(int(input())//10000))
